# 🌑 DarkGPT - Premium Telegram Bot

**Professional AI Telegram Bot powered by Custom Claude Opus API**

## ✨ Features

- 🤖 **Claude Opus AI** - Most powerful AI model
- 💾 **Conversation Memory** - Remembers complete chat history
- 🇮🇳 **Multi-Language** - Hindi, English, Hinglish, Spanish, French, German
- 🖼️ **Image Generation** - Create images from text
- 🎥 **Video Generation** - Generate videos
- 🌐 **Real-time Data** - Access to current information
- ⚡ **Fast Responses** - Professional-grade performance

## 🚀 Quick Setup (2 Minutes)

### 1️⃣ Get Telegram Bot Token (FREE)

1. Open Telegram → Search `@BotFather`
2. Send `/newbot`
3. Name: `DarkGPT`
4. Username: `yourname_darkgpt_bot`
5. Copy token: `7123456:AAHdqTcvCH...`

### 2️⃣ Local Test (Optional)

```bash
git clone https://github.com/Aman262626/DarkGPT-Telegram-Bot.git
cd DarkGPT-Telegram-Bot
pip install -r requirements.txt
```

Create `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_token_here
```

Run bot:
```bash
python bot.py
```

### 3️⃣ Deploy on Render (24/7 Free Hosting)

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. New → Web Service
4. Connect this repo: `DarkGPT-Telegram-Bot`
5. Add Environment Variable:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: (your telegram token)
6. Click "Create Web Service"

**Done! Bot is live 24/7** 🎉

## 🎮 Commands

- `/start` - Welcome message & features
- `/clear` - Reset conversation history
- `/help` - Detailed help menu

## 💡 Example Usage

**Text Conversations:**
```
You: Hello! Aap kaun hain?
Bot: Main DarkGPT hoon, Claude Opus AI se powered...

You: Python mein function kaise likhte hain?
Bot: Python mein function banana bahut simple hai...
```

**Image Generation:**
```
You: Generate an image of a sunset over mountains
Bot: [AI will generate and provide image]
```

**Multi-language:**
```
You: Bonjour! Comment ça va?
Bot: Bonjour! Je vais bien, merci...
```

## 🔧 Tech Stack

- Python 3.8+
- python-telegram-bot 20.7
- Custom Claude Opus API
- Requests library
- python-dotenv

## 🎯 API Features

Your custom API endpoint: `https://claude-opus-chatbot.onrender.com/chat`

**Supported Features:**
- ✅ Conversation Memory
- ✅ Image Generation
- ✅ Video Generation
- ✅ Multi-language (6+ languages)
- ✅ Real-time Data Access
- ✅ Professional Edition (v7.0.0)

## ❓ Troubleshooting

**Bot not responding?**
- Check if bot token is correct
- Verify API endpoint is operational
- Check Render logs for errors

**API Error?**
- Custom API might be starting up (wait 1-2 min)
- Check API status at base URL
- Verify network connection

**Slow responses?**
- Claude Opus provides detailed responses
- Image/video generation takes time
- Normal for complex queries

## 📝 License

MIT License - Free to use

## 👤 Developer

[@Aman262626](https://github.com/Aman262626)

## 🔗 API Documentation

API Endpoint: `https://claude-opus-chatbot.onrender.com`

**Endpoints:**
- `GET /` - API status
- `POST /chat` - Main chat endpoint
- `GET /health` - Health check

**Request Format:**
```json
{
  "message": "Your question here",
  "conversation_history": [...],
  "user_id": "unique_user_id"
}
```

**Response Format:**
```json
{
  "response": "AI generated response"
}
```

---

⭐ Star this repo if you find it helpful!