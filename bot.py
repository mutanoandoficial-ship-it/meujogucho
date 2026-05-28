import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8908935616:AAGFX8oFTqeuADfB_7R0qSGWQgglZU5PQIk"
GAME_SHORT_NAME = "saladando"
GAME_URL = "https://mutanoandoficial-ship-it.github.io/meujogucho/" # Link do seu GitHub Pages

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=GAME_SHORT_NAME)

async def game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.game_short_name == GAME_SHORT_NAME:
        await query.answer(url=GAME_URL)

async def main():
    # Inicializa o bot de forma totalmente assíncrona
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(game_callback))
    
    await app.initialize()
    await app.updater.start_polling()
    await app.start()
    
    print("Bot rodando com sucesso!")
    # Mantém o bot vivo em segundo plano
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    # Usa a forma correta de rodar assincronamente no Python moderno
    asyncio.run(main())
