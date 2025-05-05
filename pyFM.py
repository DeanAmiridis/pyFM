import requests
import sys

API_KEY = ""  # Replace this with your API key (https://www.last.fm/api/account/create)
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_recent_tracks(username, limit=50, max_pages=3): # max_pages (3 x 50 = 150 tracks) - API Limit is 200
    all_tracks = []
    for page in range(1, max_pages + 1):
        params = {
            "method": "user.getrecenttracks",
            "user": username,
            "api_key": API_KEY,
            "format": "json",
            "limit": limit,
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        tracks = response.json().get('recenttracks', {}).get('track', [])
        if not tracks:
            break
        for track in tracks:
            name = track['name']
            artist = track['artist']['#text']
            date = track.get('date', {}).get('#text', 'Now Playing')
            all_tracks.append({'track': name, 'artist': artist, 'time': date})
    return all_tracks

def get_top_tracks(username, limit=50, max_pages=3):
    all_tracks = []
    for page in range(1, max_pages + 1):
        params = {
            "method": "user.gettoptracks",
            "user": username,
            "api_key": API_KEY,
            "format": "json",
            "limit": limit,
            "page": page
        }
        response = requests.get(BASE_URL, params=params)
        tracks = response.json().get('toptracks', {}).get('track', [])
        if not tracks:
            break
        for track in tracks:
            name = track['name']
            artist = track['artist']['name']
            plays = track['playcount']
            all_tracks.append({'track': name, 'artist': artist, 'plays': plays})
    return all_tracks
    
def format_markdown_table(data, headers):
    header_row = '| ' + ' | '.join(headers) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    rows = [header_row, separator]

    for item in data:
        row = '| ' + ' | '.join([str(item[h.lower()]) for h in headers]) + ' |'
        rows.append(row)
    return '\n'.join(rows)

def main(profile_url):
    username = profile_url.rstrip('/').split('/')[-1]
    
    recent = get_recent_tracks(username)
    top = get_top_tracks(username)

    md_output = []

    md_output.append(f"## Recent Tracks for **{username}**\n")
    md_output.append(format_markdown_table(recent, ['Track', 'Artist', 'Time']))
    
    md_output.append(f"\n\n## Top Tracks for **{username}** (All Time)\n")
    md_output.append(format_markdown_table(top, ['Track', 'Artist', 'Plays']))

    markdown_text = '\n'.join(md_output)

    # Save to file
    output_filename = f"{username}_lastfm_stats.md"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

    # Print to terminal
    print(markdown_text)
    print(f"\n✅ Markdown saved to: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pyFM.py https://www.last.fm/user/USERNAME")
    else:
        main(sys.argv[1])
