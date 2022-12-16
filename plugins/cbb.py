# (©)Codexbotz
# Recode by @Cyberhunt27

from pyrogram import __version__
from bot import Bot
from config import CHANNEL, OWNER
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>🥷 ᴘᴇᴍʙᴜᴀᴛ : <a href='https://t.me/Cyberhunt27'>ᴏʀᴀɴɢ ɪɴɪ</a>\n🔗 Language : <code>Python3</code>\n🔗 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n🔗 Channel : @SkyBotId\n🔗 Support Group : @Skybotsupport</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴜᴛᴜᴘ •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
