#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K & PR0FESS0R-99

import os
from config import Config
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION_TEXT=Config.CAPTION
BUTTON_TEXT=Config.BUTTON_TEXT
URL_LINK=Config.URL_LINK


@Client.on_message(filters.media & filters.channel)
async def caption(client, message: Message):
    kopp, _ = get_file_id(message)
    await message.edit(f"`{kopp.file_name}`\n<i><b>{CAPTION_TEXT}</b></i>\n\n🧐𝙁𝙧𝙚𝙖𝙠𝙚𝙧𝙨🎭𝙁𝙞𝙡𝙢𝙮™🍿©\n 100% ғᴀꜱᴛ & ϙᴜᴀʟɪᴛʏ\n▬▬▬▬▬▬▬▬▬▬▬▬",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(f"{BUTTON_TEXT}", url=f"{URL_LINK}")
              ]]
        ))

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                return obj, obj.file_id
