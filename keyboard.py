from aiogram import types


def more():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Новый анекдот🆕", callback_data='more')
    keyboard.add(button)
    return keyboard
