from aiogram.utils.keyboard import InlineKeyboardBuilder

# Main menu
main_menu = InlineKeyboardBuilder()
main_menu.button(text="Социалистический город", callback_data="social_city")
main_menu.button(text="Капиталистический город", callback_data="capital_city")
main_menu.button(text="Сравнительный анализ", callback_data="compare_analytics")
main_menu.button(text="Источники", callback_data="sources")
main_menu = main_menu.adjust(1, 1, 1, 1).as_markup()  # width of each row

# Back button to start menu
to_main_menu = InlineKeyboardBuilder()
to_main_menu.button(text="Back", callback_data="main_menu")
to_main_menu = to_main_menu.as_markup()
