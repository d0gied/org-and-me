from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.media_group import MediaGroupBuilder

from utils import keyboards, texts, filters

from . import capital_city, social_city

router = Router(name=__name__)
router.include_router(capital_city.router)
router.include_router(social_city.router)


@router.message(Command("start"))
async def start(message: Message):
    media_group = MediaGroupBuilder(caption=texts.MAIN_MENU)
    media_group.add_photo(media="https://picsum.photos/200/300")
    await message.answer_photo(
        photo="https://picsum.photos/200/300",
        caption=texts.MAIN_MENU,
        reply_markup=keyboards.main_menu,
    )
    await message.delete()


@router.callback_query(filters.CallbackData("social_city"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.SOCIAL_CITY, reply_markup=keyboards.social_city
    )


@router.callback_query(filters.CallbackData("capital_city"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.CAPITAL_CITY, reply_markup=keyboards.capital_city
    )


@router.callback_query(filters.CallbackData("compare_analytics"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.COMPARE_ANALYTICS, reply_markup=keyboards.to_main_menu
    )


@router.callback_query(filters.CallbackData("sources"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.SOURCES, reply_markup=keyboards.to_main_menu
    )


@router.callback_query(filters.CallbackData("main_menu"))
async def back_to_main_menu(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.MAIN_MENU, reply_markup=keyboards.main_menu
    )
