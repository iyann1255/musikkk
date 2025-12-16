# MusicBot Yukki-style (Custom)

## Ringkas
- /play satu pintu:
  - URL stream (m3u8/mp3/radio) => diputar di Voice Chat
  - YouTube (judul/link) => search + tombol Open (tanpa scraping/robots.txt)
- /cplay untuk target channel/group

## Wajib
- Python 3.10+
- FFmpeg terpasang:
  sudo apt update && sudo apt install -y ffmpeg

## ENV
API_ID=...
API_HASH=...
BOT_TOKEN=...
ASSISTANT_SESSION=...
YOUTUBE_API_KEY=...   (opsional; kalau kosong fallback ke tombol Open Search)
OWNER_ID=...

## Run
pip install -r requirements.txt
python main.py
