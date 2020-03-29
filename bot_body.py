from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from settings import *
import logging


updater = Updater(token=BOT_TOKEN, use_context=True)
disp = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(upd, context):
    context.bot.send_message(chat_id=upd.effective_chat.id, text="hello, gays")


start_handler = CommandHandler('start', start)
disp.add_handler(start_handler)

updater.start_polling()


def echo(upd, context):
    context.bot.send_message(chat_id=upd.effective_chat.id, text=upd.message.text)


echo_handler = MessageHandler(Filters.text, echo)
disp.add_handler(echo_handler)


def caps(upd, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=upd.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
disp.add_handler(caps_handler)


def inline_caps(upd, context):
    query = upd.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(upd.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
disp.add_handler(inline_caps_handler)


def unknown(upd, context):
    context.bot.send_message(chat_id=upd.effective_chat.id, text='sry')


unknown_handler = MessageHandler(Filters.command, unknown)
disp.add_handler(unknown_handler)
