from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from utils import keyboards, texts, filters

router = Router(name=__name__)


@router.callback_query(filters.CallbackData("social_area_planing"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_media(
        media=types.InputMediaPhoto(
            media=texts.SOCIAL_AREA_PLANING_PHOTO, caption=texts.SOCIAL_AREA_PLANING
        ),
        reply_markup=keyboards.to_social_city,
    )


@router.callback_query(filters.CallbackData("social_culture"))
async def culture(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_media(
        media=types.InputMediaPhoto(
            media=texts.SOCIAL_CULTURE_PHOTO, caption=texts.SOCIAL_CULTURE
        ),
        reply_markup=keyboards.to_social_city,
    )


@router.callback_query(filters.CallbackData("social_economy"))
async def economy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.SOCIAL_ECONOMY, reply_markup=keyboards.to_social_city
    )


@router.callback_query(filters.CallbackData("social_social_policy"))
async def social_policy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_caption(
        caption=texts.SOCIAL_SOCIAL_POLICY, reply_markup=keyboards.to_social_city
    )
