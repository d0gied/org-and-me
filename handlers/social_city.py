from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from utils import filters, keyboards, texts

router = Router(name=__name__)


@router.callback_query(filters.CallbackData("social_info"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.SOCIAL_INFO_PHOTO)
    await message.answer(texts.SOCIAL_INFO)


@router.callback_query(filters.CallbackData("social_area_planing"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.SOCIAL_AREA_PLANING_PHOTO)
    await message.answer(texts.SOCIAL_AREA_PLANING)


@router.callback_query(filters.CallbackData("social_culture"))
async def culture(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.SOCIAL_CULTURE_PHOTO)
    await message.answer(texts.SOCIAL_CULTURE)


@router.callback_query(filters.CallbackData("social_economy"))
async def economy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.SOCIAL_ECONOMY_PHOTO)
    await message.answer(texts.SOCIAL_ECONOMY)


@router.callback_query(filters.CallbackData("social_social_policy"))
async def social_policy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.SOCIAL_SOCIAL_POLICY_PHOTO)
    await message.answer(texts.SOCIAL_SOCIAL_POLICY)
