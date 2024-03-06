import re
from pyrogram import filters
import random
from Akshat import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAELoE5l6MUZAojtAUGlh-dYBt4sNvTkQQACJwwAAsgQSVeRFgyaPmSjqzQE", # Sticker 1
        "CAACAgUAAxkBAAELoFBl6MVGciDXeTLQ_KK5alkJGbZRMQACnw0AAslWSFc-mES3oOu_vzQE", # Sticker 2
        "CAACAgUAAxkBAAELoFJl6MVLxMKzqhWlxuYb5x1cINkLfgAC9xUAAmIbQFduEPo3HMUjLzQE", # Sticker 3
        "CAACAgUAAxkBAAELoFRl6MVQytSMcLyXSFiNLFMEeGhOrwACIxEAAg5HSVf9l35v6W4AAZk0BA",
        "CAACAgUAAxkBAAELoFZl6MVWmLlCGwSeIWrQtnrek5_jWQACgA0AApp5SFfLIaS_34uDVzQE",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
