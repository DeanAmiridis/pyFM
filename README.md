# 🎵 Last.fm Profile Scraper

A simple Python script that pulls **recent tracks** and **top tracks** from any public [Last.fm](https://www.last.fm/) user profile and outputs the data in a nicely formatted **Markdown table**.  

You get:
- ✅ Terminal output
- 📄 Markdown file saved locally

---

## 📦 Requirements

- Python 3.6+
- A Last.fm API key (free): [Get it here](https://www.last.fm/api/account/create)

### 🧪 Install Dependencies

```bash
pip install requests
```

---

## 🚀 Usage

```bash
python main.py https://www.last.fm/user/your_username
```

### 🧠 Example

```bash
python main.py https://www.last.fm/user/dean_fx
```

📄 This will:
- Print recent & top tracks to the terminal
- Save a file like: `dean_fx_lastfm_stats.md`

---

## 🔑 Setup Your API Key

Edit the script and replace the `API_KEY` variable at the top:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## 🛠 Features

- 📥 Fetches **up to hundreds** of recent and top tracks (via paginated API calls)
- 💾 Saves Markdown output to file in current directory
- 💬 Displays output in terminal for easy copy/paste
- 🔓 Works with any **public** Last.fm user — no auth required

---

## 📚 Example Output

```markdown
## Recent Tracks for **dean_fx**

| Track | Artist | Time |
| --- | --- | --- |
| Hypnotize | Psycho Boys Club | 30 Apr 5:08pm |
...

## Top Tracks for **dean_fx** (All Time)

| Track | Artist | Plays |
| --- | --- | --- |
| One More Time | Daft Punk | 132 |
...
```

---

## ❤️ Credits

Made with 🎧 by Dean Amiridis

---

## 🧼 License

MIT
