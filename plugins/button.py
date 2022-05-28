# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="💎About Me💎", callback_data="about"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🚻 ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="💎About Me💎", callback_data="about"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="💎About Me💎", callback_data="about"),
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="💎About Me💎", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="▶️ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
                InlineKeyboardButton(text="🚻 ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🚻 ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="🚻 ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
#---------------------------------
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink1),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelinkch2),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelinkch3),
                InlineKeyboardButton(text="🚻 ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink1),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelinkch2),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelinkch3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
        
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL2 and not FORCE_SUB_CHANNEL3 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelinkch2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_CHANNEL3 and not FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=client.invitelink),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelinkch3),

            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

    if FORCE_SUB_CHANNEL2 and FORCE_SUB_CHANNEL3 and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=client.invitelinkch2),
                InlineKeyboardButton(text="▶️ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=client.invitelinkch3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔁 Try Again",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons

