import os

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Assistant user account session string (wajib untuk join voice chat)
ASSISTANT_SESSION = os.getenv("ASSISTANT_SESSION", "")

# YouTube Data API (untuk search metadata, bukan streaming)
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

OWNER_ID = int(os.getenv("OWNER_ID", "0"))
