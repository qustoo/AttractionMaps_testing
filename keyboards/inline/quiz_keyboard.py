from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import place_callback

choice_r_q = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton
                (
                text="Советский",
                callback_data=place_callback.new(item_name="sov_r_q")
            ),
            InlineKeyboardButton
                (
                text="Кировский",
                callback_data=place_callback.new(item_name="kir_r_q")
            ),
            InlineKeyboardButton
                (
                text="Октябрьский",
                callback_data=place_callback.new(item_name="oct_r_q")
            ),

        ],
        [
            InlineKeyboardButton
                (
                text="Железнодорожный",
                callback_data=place_callback.new(item_name="rai_r_q")
            ), InlineKeyboardButton
            (
            text="Ворошиловский",
            callback_data=place_callback.new(item_name="vor_r_q")
        )
        ],
        [
            InlineKeyboardButton
                (
                text="Ленинский",
                callback_data=place_callback.new(item_name="len_r_q")
            ),
            InlineKeyboardButton
                (
                text="Первомайский",
                callback_data=place_callback.new(item_name="perv_r_q")
            ),
            InlineKeyboardButton
                (
                text="Пролетарский",
                callback_data=place_callback.new(item_name="prol_r_q")
            )
        ],
        {
            InlineKeyboardButton
                (
                text="Отмена",
                callback_data="cancel_place_r_q"
            )
        }
    ]
)
