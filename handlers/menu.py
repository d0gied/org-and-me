from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InputMediaPhoto, Message
from aiogram.utils.media_group import MediaGroupBuilder

from utils import filters, keyboards, texts

from . import capital_city, social_city

router = Router(name=__name__)
router.include_router(capital_city.router)
router.include_router(social_city.router)


@router.message(Command("start", "menu"))
async def start(message: Message):
    await message.answer_photo(
        photo=texts.MAIN_MENU_PHOTO,
        caption=texts.MAIN_MENU,
        reply_markup=keyboards.main_menu,
    )
    await message.delete()


@router.callback_query(filters.CallbackData("social_city"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_media(
        media=InputMediaPhoto(media=texts.SOCIAL_CITY_PHOTO, caption=texts.SOCIAL_CITY),
        reply_markup=keyboards.social_city,
    )


@router.callback_query(filters.CallbackData("capital_city"))
async def menu2(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_media(
        media=InputMediaPhoto(media=texts.CAPITAL_CITY_PHOTO, caption=texts.CAPITAL_CITY),
        reply_markup=keyboards.capital_city,
    )


@router.callback_query(filters.CallbackData("compare_analytics"))
async def menu3(callback_query: types.CallbackQuery):
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


@router.callback_query(filters.CallbackData("authors"))
async def menu1(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer('<a href="https://t.me/d0gied">Новоходский Герман</a>')
    await message.answer('<a href="https://t.me/khadzakos">Хадзакос Николай</a>')
    await message.answer('<a href="https://t.me/russiankolya">Федоров Николай</a>')


@router.callback_query(filters.CallbackData("main_menu"))
async def back_to_main_menu(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_media(
        media=InputMediaPhoto(media=texts.MAIN_MENU_PHOTO, caption=texts.MAIN_MENU),
        reply_markup=keyboards.main_menu,
    )
