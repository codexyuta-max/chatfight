from bot.client import app

# ─────────────────────────────
# Fake Web Server (Render needs this)
# ─────────────────────────────
from flask import Flask
import threading
import os

web = Flask(__name__)

@web.route("/")
def home():
    return "🔥 ChatFight Bot is alive!"

def run_web():
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT
    web.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web, daemon=True).start()

# FORCE IMPORT ALL HANDLERS
import bot.handlers.ranking
import bot.handlers.admin
import bot.handlers.start
import bot.handlers.counter

# ─────────────────────────────
# Start Bot
# ─────────────────────────────
print("🔥 ChatFight Bot is running...")
app.run()
