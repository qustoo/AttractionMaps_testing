from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import place_callback, pagination_call

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
                text="Октябрьский",
                callback_data=place_callback.new(item_name="oct_r")
            ),
            InlineKeyboardButton
                (
                text="Ленинский",
                callback_data=place_callback.new(item_name="len_r")
            ),
        ],
        [

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

def get_page_keyboard(k:str,max:int,page:int=1):
    previous_page=page-1
    previous_page_text="<< "
    current_page_text=f"<{page}>"
    next_page = page+1
    next_page_text=" >>"
    markup=InlineKeyboardMarkup()
    if previous_page>0:
        markup.insert(InlineKeyboardButton
                      (text=previous_page_text,
                       callback_data=pagination_call.new(key=k, page=previous_page))
                       )
    markup.insert(InlineKeyboardButton
                  (text=current_page_text,
                   callback_data=pagination_call.new(key=k, page="current_page")
                   )
                  )
    if page < max:
        markup.insert(InlineKeyboardButton
                      (text=next_page_text,
                       callback_data=pagination_call.new(key=k, page=next_page)
                       )
                      )
    if previous_page>0:
        markup.insert(InlineKeyboardButton
                      (text="начало",
                       callback_data=pagination_call.new(key=k, page=1))
                      )

    return markup


def get_text(k:str,max:int,page:int=1):
    previous_page = page - 1
    previous_page_text = "<< "
    current_page_text = f"<{page}>"
    next_page = page + 1
    next_page_text = " >>"
    markup = InlineKeyboardMarkup()
    if previous_page > 0:
        markup.insert(InlineKeyboardButton
                      (text=previous_page_text,
                       callback_data=pagination_call.new(key=k, page=previous_page))
                      )
    markup.insert(InlineKeyboardButton
                  (text=current_page_text,
                   callback_data=pagination_call.new(key=k, page="current_page")
                   )
                  )
    if page < max:
        markup.insert(InlineKeyboardButton
                      (text=next_page_text,
                       callback_data=pagination_call.new(key=k, page=next_page)
                       )
                      )
    if previous_page > 0:
        markup.insert(InlineKeyboardButton
                      (text="начало",
                       callback_data=pagination_call.new(key=k, page=1))
                      )

    return markup
