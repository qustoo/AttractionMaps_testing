from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import place_callback

choice_p = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton
                (
                text="Советский",
                callback_data=place_callback.new(item_name="sov_r", scale=1000)
            ),
            InlineKeyboardButton
                (
                text="Кировский",
                callback_data=place_callback.new(item_name="zh_r", scale=1000)
            ),
            InlineKeyboardButton
                (
                text="Октябрьский",
                callback_data=place_callback.new(item_name="okt_r", scale=1000)
            ),

        ],
        [
            InlineKeyboardButton
                (
                text="Железнодорожный",
                callback_data=place_callback.new(item_name="len_r", scale=1000)
            ), InlineKeyboardButton
            (
            text="Ворошиловский",
            callback_data=place_callback.new(item_name="kir_r", scale=1000)
        )
        ],
        [
            InlineKeyboardButton
                (
                text="Ленинский",
                callback_data=place_callback.new(item_name="vor_r", scale=1000)
            ),
            InlineKeyboardButton
                (
                text="Первомайский",
                callback_data=place_callback.new(item_name="perv_r", scale=1000)
            ),
            InlineKeyboardButton
                (
                text="Пролетарский",
                callback_data=place_callback.new(item_name="prol_r", scale=1000)
            )
        ],
        [
            InlineKeyboardButton
                (
                text="Отмена",
                callback_data="cancel_place"
            )
        ]
    ]
)

place_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name=1, scale=1000)),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name=2, scale=1000)),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name=3, scale=1000))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name=4, scale=1000)),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name=5, scale=1000)),
     InlineKeyboardButton(text="Show more", callback_data=place_callback.new(item_name="show_more", scale=1000))]
])
