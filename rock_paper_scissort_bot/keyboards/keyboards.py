from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import LEXICON_RU

yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

button_yes: KeyboardButton = KeyboardButton(LEXICON_RU['yes_button'])
button_no: KeyboardButton = KeyboardButton(LEXICON_RU['no_button'])

yes_no_kb.add(button_yes, button_no)

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)

button_1: KeyboardButton = KeyboardButton(LEXICON_RU['rock'])
button_2: KeyboardButton = KeyboardButton(LEXICON_RU['scissors'])
button_3: KeyboardButton = KeyboardButton(LEXICON_RU['paper'])

game_kb.add(button_1).add(button_2).add(button_3)

