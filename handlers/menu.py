from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from utils import keyboards, texts

router = Router(name=__name__)


class CallbackData:
    def __init__(self, *commands) -> None:
        self.commands = []
        for command in commands:
            if isinstance(command, str):
                self.commands.append(command)
            elif isinstance(command, list):
                self.commands.extend(command)
            else:  # pragma: no cover
                raise TypeError(
                    "CallbackData() argument must be a string or a list of strings."
                )

    def __call__(self, query: CallbackQuery):
        return query.data in self.commands


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=texts.MAIN_MENU, reply_markup=keyboards.main_menu)


@router.callback_query(CallbackData("menu1"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.MENU_1, reply_markup=keyboards.to_main_menu)


@router.callback_query(CallbackData("menu2"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.MENU_2, reply_markup=keyboards.to_main_menu)


@router.callback_query(CallbackData("menu3"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.MENU_3, reply_markup=keyboards.to_main_menu)


@router.callback_query(CallbackData("main_menu"))
async def back_to_main_menu(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.MAIN_MENU, reply_markup=keyboards.main_menu)
