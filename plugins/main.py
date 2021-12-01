import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import time
import os
import sqlite3
import asyncio

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

import pyrogram

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="⚙️ Help", callback_data="help"),
        InlineKeyboardButton(text="🤖 About", callback_data="about"),
        ],[
        InlineKeyboardButton(text="Close 🔐", callback_data="close")
        ]]
    )

@Client.on_message(pyrogram.filters.command(["start"]))
async def text(bot, update):
    await update.reply_text(Translation.START_TEXT.format(update.from_user.first_name),
        reply_markup= START_BUTTONS,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["help"]))
def help_user(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Support 👥", url="https://t.me/SDBOTz")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["about"]))
def about(bot, update):
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Report Bug 🐞", url="https://t.me/SDBOTz")]]),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )
