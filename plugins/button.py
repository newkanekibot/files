# Credits: @Cyberhunt27

from config import FORCE_SUB_CHANNEL
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="🥷 ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
                InlineKeyboardButton(text="🔐 ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    #if FORCE_SUB_CHANNEL:
    #    buttons = [
    #        [
    #            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
    #        ],
    #        [
    #            InlineKeyboardButton(text="🥷 ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
    #            InlineKeyboardButton(text="🔐 ᴛᴜᴛᴜᴘ", callback_data="close"),
    #        ],
    #    ]
    #    return buttons
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="🥷 ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [InlineKeyboardButton(text="🔐 ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    #if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
    #    buttons = [
    #        [
    #            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
    #        ],
    #    ]
    #    try:
    #        buttons.append(
    #            [
    #                InlineKeyboardButton(
    #                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
    #                    url=f"https://t.me/{client.username}?start={message.command[1]}",
    #                )
    #            ]
    #        )
    #    except IndexError:
    #        pass
    #    return buttons
