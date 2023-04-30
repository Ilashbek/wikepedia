
import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang('uz')

API_TOKEN = '6287219455:AAFz74qNdB8avRmCghNIospWUGyRYKGumKE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#/start kamandasi uchun hendler
@dp.message_handler(commands="Boshlash")
async def select_start(message:types.Message):
    await message.answer(f"Assalomu alaykum @{message.from_user.username} wikipediya botga xush kelibsiz")

#help buyrug'i uchun hendler
@dp.message_handler(commands="help")
async def select_start(message:types.Message):
    await message.answer(f"salom @{message.from_user.username} ushbu botga xar qanday suz yoki matn kiritishingiz mumkin ")

#tutiqush handlers
wikipedia.set_lang('uz')
@dp.message_handler()
async def echo_handler(message:types.Message):
    try:
        javob=wikipedia.summary(message)
        await message.answer(javob)
    except:
        await message.answer("Bunday malumot topilmadi Iltimos suzlarni tug'irlab matn kurinishda yozing")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)