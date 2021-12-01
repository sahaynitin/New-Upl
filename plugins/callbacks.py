import pyrogram

from pyrogram import Client as pyrogram, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant

from translation import Translation


helpbutton = [[
        InlineKeyboardButton(f'📣 Channel 📣', url="https://t.me/SDBOTs_inifinity"),
        InlineKeyboardButton(f'🙋‍♀️ Support 🙋‍♀️', url="https://t.me/SDBOTz")
        ],[
        InlineKeyboardButton(f'🤖 About', callback_data="about")
    ]]

aboutbutton = [[
        InlineKeyboardButton(f'🤔 How To Use', callback_data="help"),
        InlineKeyboardButton(f'Close 🔐', callback_data="close_data")
    ]]


   
@Client.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)
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
