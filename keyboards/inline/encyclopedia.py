from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import place_callback

choice_p = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton
                (
                text="Советский",
                callback_data=place_callback.new(item_name="sov_r")
            ),
            InlineKeyboardButton
                (
                text="Кировский",
                callback_data=place_callback.new(item_name="kir_r")
            ),
            InlineKeyboardButton
                (
                text="Октябрьский",
                callback_data=place_callback.new(item_name="oct_r")
            ),

        ],
        [
            InlineKeyboardButton
                (
                text="Железнодорожный",
                callback_data=place_callback.new(item_name="rai_r")
            ), InlineKeyboardButton
            (
            text="Ворошиловский",
            callback_data=place_callback.new(item_name="vor_r")
        )
        ],
        [
            InlineKeyboardButton
                (
                text="Ленинский",
                callback_data=place_callback.new(item_name="len_r")
            ),
            InlineKeyboardButton
                (
                text="Первомайский",
                callback_data=place_callback.new(item_name="perv_r")
            ),
            InlineKeyboardButton
                (
                text="Пролетарский",
                callback_data=place_callback.new(item_name="prol_r")
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
#клавиатура для советского района
soviet_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name=1)),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name=2)),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name=3))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name=4)),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name=5)),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more"))]
])
#клавиатура для октябрьского района
oct_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1ok")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2ok")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3ok"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4ok")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5ok")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_ok"))]
])
#клавиатура для пролетарского района
prolet_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1pr")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2pr")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3pr"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4pr")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5pr")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_pr"))]
])
#клавиатура для кировского района
kirov_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1kir")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2kir")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3kir"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4kir")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5kir")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_kir"))]
])
#клавиатура для ленинского района
len_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1len")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2len")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3len"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4len")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5len")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_len"))]
])
#клавиатура для железнодорожного района
rai_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1rai")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2rai")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3rai"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4rai")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5rai")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_rai"))]
])
#клавиатура для ворошиловского района
vor_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1vor")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2vor")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3vor"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4vor")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5vor")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_vor"))]
])
#клавиатура для первомайского района
per_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="1️⃣", callback_data=place_callback.new(item_name="1per")),
    InlineKeyboardButton(text="2️⃣", callback_data=place_callback.new(item_name="2per")),
    InlineKeyboardButton(text="3️⃣", callback_data=place_callback.new(item_name="3per"))],
    [InlineKeyboardButton(text="4️⃣", callback_data=place_callback.new(item_name="4per")),
     InlineKeyboardButton(text="5️⃣", callback_data=place_callback.new(item_name="5per")),
     InlineKeyboardButton(text="Показать еще", callback_data=place_callback.new(item_name="show_more_per"))]
])