from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choiсe_attractions = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Церковь"
        ),
        InlineKeyboardButton
            (
            text="Музей"
        )
    ],
    [
        InlineKeyboardButton
            (
            text="Отмена"
        )
    ]

])

print(choiсe_attractions)
print(choiсe_attractions["inline_keyboard"][-1])
print('0', choiсe_attractions.inline_keyboard[0])
new_keyb = InlineKeyboardMarkup(row_width=1,inline_keyboard=[])
print(choiсe_attractions["inline_keyboard"][-1])
print(choiсe_attractions["inline_keyboard"][0][0])
print('sasasa',choiсe_attractions["inline_keyboard"][0])
print('list =',choiсe_attractions["inline_keyboard"][0][-1])
print('012112',choiсe_attractions.inline_keyboard)
new_keyb.inline_keyboard.append({choiсe_attractions["inline_keyboard"][0][0],choiсe_attractions["inline_keyboard"][0][1]})
new_keyb.inline_keyboard.append({choiсe_attractions["inline_keyboard"][-1][-1]})
print(new_keyb)
