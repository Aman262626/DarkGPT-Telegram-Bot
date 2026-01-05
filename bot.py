import os
import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from collections import defaultdict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom API endpoint
API_URL = "https://claude-opus-chatbot.onrender.com/chat"

# Conversation memory storage
user_conversations = defaultdict(list)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command handler"""
    welcome_message = (
        "🌑 *DarkGPT - Premium AI Platform*\n\n"
        "Features:\n"
        "✅ Claude Opus AI - Most Powerful\n"
        "✅ Conversation Memory\n"
        "✅ Image Generation\n"
        "✅ Video Generation\n"
        "✅ Multi-Language Support\n"
        "✅ Real-time Data Access\n\n"
        "Commands:\n"
        "/start - Bot shuru karo\n"
        "/clear - Chat history clear karo\n"
        "/help - Help menu\n\n"
        "💬 Kuch bhi pucho, DarkGPT ready hai!"
    )
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear conversation history"""
    user_id = update.effective_user.id
    user_conversations[user_id] = []
    await update.message.reply_text("🌑 Chat history successfully cleared!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = (
        "*DarkGPT Help Menu* 🌑\n\n"
        "📌 *Kaise use kare:*\n"
        "• Seedhe apna question type karo\n"
        "• Bot previous messages yaad rakhega\n"
        "• Hindi, English, Hinglish - sabhi supported\n"
        "• Image generation support hai\n"
        "• Video generation bhi available\n"
        "• Real-time data access\n\n"
        "📌 *Commands:*\n"
        "/start - Welcome message\n"
        "/clear - Conversation reset\n"
        "/help - Ye menu\n\n"
        "⚡ *Powered by Claude Opus* - Professional Edition"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user messages"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Typing indicator
    await update.message.chat.send_action("typing")
    
    try:
        # Add user message to conversation history
        user_conversations[user_id].append({
            "role": "user",
            "content": user_message
        })
        
        # Keep only last 20 messages for context
        if len(user_conversations[user_id]) > 20:
            user_conversations[user_id] = user_conversations[user_id][-20:]
        
        # Prepare API request
        payload = {
            "message": user_message,
            "conversation_history": user_conversations[user_id][:-1],
            "user_id": str(user_id)
        }
        
        # Call custom API
        response = requests.post(
            API_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        if response.status_code == 200:
            data = response.json()
            bot_response = data.get("response", data.get("message", "No response received"))
            
            # Add bot response to history
            user_conversations[user_id].append({
                "role": "assistant",
                "content": bot_response
            })
            
            # Send response
            await update.message.reply_text(bot_response)
        else:
            await update.message.reply_text(
                f"❌ API Error: {response.status_code}\n"
                "Kripya phir se try karo."
            )
        
    except requests.exceptions.Timeout:
        await update.message.reply_text(
            "❌ Request timeout! API respond nahi kar raha.\n"
            "Thodi der baad try karo."
        )
    except requests.exceptions.RequestException as e:
        logger.error(f"Request Error: {e}")
        await update.message.reply_text(
            "❌ Network error! Connection problem hai.\n"
            "Kripya phir se try karo."
        )
    except Exception as e:
        logger.error(f"Error: {e}")
        await update.message.reply_text(
            "❌ Error occurred! Kripya phir se try karo.\n"
            "Agar problem continue ho to /clear karke naye conversation start karo."
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    # Get token from environment
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN environment variable not set!")
    
    # Create application
    app = Application.builder().token(token).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)
    
    # Start bot
    logger.info("🌑 DarkGPT Bot starting with custom Claude Opus API...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()