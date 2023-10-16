from aiogram.utils.keyboard import InlineKeyboardBuilder

# Main menu
main_menu = InlineKeyboardBuilder()
main_menu.button(text="Социалистический город", callback_data="social_city")
main_menu.button(text="Капиталистический город", callback_data="capital_city")
main_menu.button(text="Сравнительный анализ", callback_data="compare_analytics")
main_menu.button(text="Авторы", callback_data="authors")
main_menu = main_menu.adjust(1, 1, 1, 1).as_markup()  # width of each row

# Back button to start menu
to_main_menu = InlineKeyboardBuilder()
to_main_menu.button(text="Назад", callback_data="main_menu")
to_main_menu = to_main_menu.as_markup()

# social_city
social_city = InlineKeyboardBuilder()
social_city.button(text="Общая информация", callback_data="social_info")
social_city.button(text="Организация пространства", callback_data="social_area_planing")
social_city.button(text="Культура", callback_data="social_culture")
social_city.button(text="Экономика", callback_data="social_economy")
social_city.button(text="Социальная политика", callback_data="social_social_policy")
social_city.button(text="Назад", callback_data="main_menu")
social_city = social_city.adjust(1, 1, 1, 1, 1, 1).as_markup()  # width of each row

to_social_city = InlineKeyboardBuilder()
to_social_city.button(text="Назад", callback_data="social_city")
to_social_city = to_social_city.as_markup()

# capital_city
capital_city = InlineKeyboardBuilder()
capital_city.button(text="Общая информация", callback_data="capital_info")
capital_city.button(
    text="Организация пространства", callback_data="capital_area_planing"
)
capital_city.button(text="Культура", callback_data="capital_culture")
capital_city.button(text="Экономика", callback_data="capital_economy")
capital_city.button(text="Социальная политика", callback_data="capital_social_policy")
capital_city.button(text="Назад", callback_data="main_menu")
capital_city = capital_city.adjust(1, 1, 1, 1, 1).as_markup()  # width of each row

to_capital_city = InlineKeyboardBuilder()
to_capital_city.button(text="Назад", callback_data="capital_city")
to_capital_city = to_capital_city.as_markup()
