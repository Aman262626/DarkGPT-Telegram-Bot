# 🌑 DarkGPT - Telegram Bot

**100% FREE AI Telegram Bot powered by Google Gemini**

## ✨ Features

- 🤖 **Google Gemini AI** - Powerful FREE AI
- 💾 **Conversation Memory** - Remembers chat history
- 🌍 **Multi-Language** - Hindi, English, Hinglish
- ⚡ **Fast Responses** - Real-time replies
- 💰 **No Cost** - Completely FREE API

## 🚀 Quick Start (5 Minutes)

### 1️⃣ Get API Keys (Both FREE)

**Telegram Bot Token:**
1. Open Telegram → Search `@BotFather`
2. Send `/newbot`
3. Name: `DarkGPT`
4. Username: `yourname_darkgpt_bot`
5. Copy token: `7123456:AAHdqTcvCH...`

**Google Gemini API Key:**
1. Visit: [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy key: `AIzaSyXXXXXX...`

### 2️⃣ Local Setup

```bash
git clone https://github.com/Aman262626/DarkGPT-Telegram-Bot.git
cd DarkGPT-Telegram-Bot
pip install -r requirements.txt
```

Create `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_token_here
GEMINI_API_KEY=your_key_here
```

Run bot:
```bash
python bot.py
```

### 3️⃣ Deploy on Render (24/7 Free Hosting)

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. New → Web Service
4. Connect this repo
5. Add Environment Variables:
   - `TELEGRAM_BOT_TOKEN`
   - `GEMINI_API_KEY`
6. Click "Create Web Service"

**Done! Bot is live 24/7** 🎉

## 🎮 Commands

- `/start` - Welcome message
- `/clear` - Reset chat history
- `/help` - Help menu

## 💡 Example Usage

```
You: Hello! Aap kaun hain?
Bot: Namaste! Main DarkGPT hoon...

You: Maths ka sawal: 25 x 4 = ?
Bot: 25 x 4 = 100

You: Python mein loop kaise likhte hain?
Bot: Python mein for loop aisa likhte hain...
```

## 🔧 Tech Stack

- Python 3.8+
- python-telegram-bot
- Google Generative AI (Gemini)
- python-dotenv

## ❓ Troubleshooting

**Bot not responding?**
- Check if bot token is correct
- Verify Gemini API key is valid
- Check Render logs for errors

**API Error?**
- Gemini API has 60 requests/min limit
- Wait a minute and try again

## 📝 License

MIT License - Free to use

## 👤 Developer

[@Aman262626](https://github.com/Aman262626)

---

⭐ Star this repo if helpful!