import pyrogram

from pyrogram import Client as pyrogram, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from translation import Translation
aboutbutton = [[
        InlineKeyboardButton(f'🤔 How To Use', callback_data="help"),
        InlineKeyboardButton(f'Close 🔐', callback_data="close_data")
    ]]


@pyrogram.on_callback_query()
async def cb_handler(bot, update):
        
        await update.message.delete()

    elif update.data == "help":
        await update.answer()
        keyboard = InlineKeyboardMarkup(helpbutton)
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    elif update.data == "about":
        await update.answer()
        keyboard = InlineKeyboardMarkup(aboutbutton)
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    elif update.data == "close_data":
        await update.message.delete()
