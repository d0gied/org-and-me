from aiogram.utils.keyboard import InlineKeyboardBuilder

# Main menu
main_menu = InlineKeyboardBuilder()
main_menu.button(text="Button 1", callback_data="menu1")
main_menu.button(text="Button 2", callback_data="menu2")
main_menu.button(text="Button 3", callback_data="menu3")
main_menu = main_menu.adjust(1, 1, 1).as_markup()  # width of each row

# Back button to start menu
to_main_menu = InlineKeyboardBuilder()
to_main_menu.button(text="Back", callback_data="main_menu")
to_main_menu = to_main_menu.as_markup()
