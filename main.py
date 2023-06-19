import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from buttons import *

API_TOKEN = '5928753204:AAEM8Aj7mb2ioDQ_l7z3pOfa7OocCg-O59w'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup=fanlar_inline_keyboard)


# Matematika
@dp.callback_query_handler(text = "Matematika")
async def echo(call: types.CallbackQuery):
    
    await call.message.answer_poll(
        question="8*9",
        options=["25","72","10"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="55+(6*7)",
        options=["97","95","100"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="8+7*5",
        options=["43","45","40"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="4+8/2",
        options=["6","10","8"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="125/5*8",
        options=["550","200","220"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz",
        reply_markup=fanlar_inline_keyboard
    )

# Ona tili
@dp.callback_query_handler(text = "Ona tili")
async def echo(call: types.CallbackQuery):
    
    await call.message.answer_poll(
        question="1. Nutq nimalardan tuziladi ?",
        options=["Gaplardan"," So‘zlardan","Harflardan"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="2.Tartib bilan berilgan harflar………….deb  ataladi",
        options=["Tovushlar "," Alifbo","so‘zlar"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="3.Darak   gap  oxiriga qaysi tinish belgisi qo‘yiladi ?",
        options=["vergul","Undov","Nuqta"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="4.Qaysi so‘zda harf tushib qolgan ?",
        options=["Tilla","Yeti","Achchiq"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="5.Kuchli  his–hayajon bilan aytilgan  gap qanday gap deyiladi ?",
        options=["Undovgap","Darak  gap","qo‘shma  gap"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
        reply_markup=fanlar_inline_keyboard
    )
# Sport
@dp.callback_query_handler(text = "Sport")
async def echo(call: types.CallbackQuery):
    
    await call.message.answer_poll(
        question="1.  Suzish havzasining eng chuqur joyi qancha bo’lishi kerak?",
        options=["2.7"," 3","2.8"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="2.Fudbol darvozasini diametri qancha?",
        options=["22sm "," 15sm","12sm"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="3.Gandbol o’yini olimpiya o’yinlariga qachon kirib kelgan?",
        options=["1936-yil","1933-yil","1925-yil"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="4. Boks ringi o’lchami qancha bo’ladi?",
        options=["5-6m","4-5m","5-5m"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="5.Jismoniy tarbiyani kelib chiqishdagi bosh omil?",
        options=["Dehqonchilik","Ovchilik","Chorvachilik"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz",
        reply_markup=fanlar_inline_keyboard
    )

# Informatika
@dp.callback_query_handler(text = "Informatika")
async def echo(call: types.CallbackQuery):
    
    await call.message.answer_poll(
        question="1. Kompyuterning asosiy qurilmalari nimalardan iborat?",
        options=["Sistemali blok, monitor, klaviatura, sichqoncha"," Modem, printer, monitor, klaviatura ","Sistemali blok, printer, klaviatura, sichqoncha"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="2.DELETE klavishining vazifasi-",
        options=["matn yoki berilganlarni kiritish"," Matn yoki berilganlarni o'ng tomonga qarab o'chirish","Matn yoki berilganlarni chap tomonga qarab o'chirish"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz"
    )
    await asyncio.sleep(3)
    
    await call.message.answer_poll(
        question="3.Kompyuter  so’zining  ma’nosi  ?",
        options=["Lotincha  hisoblagich","Inglizcha  ma’lumot","Inglizcha  hisoblagich"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="4.Qattiq  disk  nima?",
        options=["Ma’lumotlarni  saqlovchi  xotira  qurilmasi ","Ma’lumotlarni  qog’ozga  chiqarib  beradi","A va  B  javob  to’g’ri"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz"
    )
    await asyncio.sleep(3)

    await call.message.answer_poll(
        question="5.Sistema  bloki  necha  qismdan  iborat",
        options=["4","3","5"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
        reply_markup=fanlar_inline_keyboard
    )
    await asyncio.sleep(3)












# @dp.message_handler(text = "s")
# async def echo(message: types.Message):
#     await message.answer_poll(
#         question="Kim yaxshi",
#         options=["Olim","Hakim","Tohir","Eldor"],
#         is_anonymous=False
#     )

# @dp.message_handler(text = "n")
# async def echo(message: types.Message):
#     await message.answer_poll(
#         question="Kim yaxshi",
#         options=["Olim","Hakim","Tohir","Eldor"],
#         is_anonymous=False,
#         allows_multiple_answers=True
#     )


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)