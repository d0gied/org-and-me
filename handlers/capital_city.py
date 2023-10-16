from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from utils import filters, keyboards, texts

router = Router(name=__name__)


@router.callback_query(filters.CallbackData("capital_info"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.CAPITAL_INFO_PHOTO)
    await message.answer(texts.CAPITAL_INFO)


@router.callback_query(filters.CallbackData("capital_area_planing"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.CAPITAL_AREA_PLANING_PHOTO)
    await message.answer(texts.CAPITAL_AREA_PLANING)


@router.callback_query(filters.CallbackData("capital_culture"))
async def culture(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.CAPITAL_CULTURE_PHOTO)
    await message.answer(texts.CAPITAL_CULTURE)


@router.callback_query(filters.CallbackData("capital_economy"))
async def economy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.CAPITAL_ECONOMY_PHOTO)
    await message.answer(texts.CAPITAL_ECONOMY)


@router.callback_query(filters.CallbackData("capital_social_policy"))
async def social_policy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.answer_photo(texts.CAPITAL_SOCIAL_POLICY_PHOTO)
    await message.answer(texts.CAPITAL_SOCIAL_POLICY)
