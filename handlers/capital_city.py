from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from utils import keyboards, texts, filters

router = Router(name=__name__)

@router.callback_query(filters.CallbackData("capital_area_planing"))
async def area_planing(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.CAPITAL_AREA_PLANING, reply_markup=keyboards.to_capital_city)


@router.callback_query(filters.CallbackData("capital_culture"))
async def culture(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.CAPITAL_CULTURE, reply_markup=keyboards.to_capital_city)


@router.callback_query(filters.CallbackData("capital_economy"))
async def economy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.CAPITAL_ECONOMY, reply_markup=keyboards.to_capital_city)
    
@router.callback_query(filters.CallbackData("capital_social_policy"))
async def social_policy(callback_query: types.CallbackQuery):
    message = callback_query.message
    await message.edit_text(text=texts.CAPITAL_SOCIAL_POLICY, reply_markup=keyboards.to_capital_city)
