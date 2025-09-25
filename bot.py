from aiogram import Bot, Dispatcher, types,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8429983629:AAFyk9p5fS4M4G8i5HGdDqbeiRNBCzaoN_g"
CHANNELS = ["@Tarjima_kinolar_uzb_tilda_z"]  # Majburiy obuna kanallari
ADMINS = [6000119173]
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def check_subs(user_id: int) -> bool:
    for channel in CHANNELS:
        chat_member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        if chat_member.status in ["left", "kicked"]:
            return False
    return True

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if not await check_subs(user_id):
        instagram='kino.dunyouz'
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [
                [InlineKeyboardButton(text=f"{instagram}",url=f"https://www.instagram.com/kino.dunyouz?igsh=MTdvdmJla2psaWhpMA==")],  
                [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]
            ]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
    else:
        await message.answer("Xush kelibsiz! Botdan foydalanishingiz mumkin. Kino kodini kiriting")

@dp.callback_query(lambda call: call.data == "check_subs")
async def check_subs_callback(call: types.CallbackQuery):
    user_id = call.from_user.id
    if await check_subs(user_id):
        await call.message.edit_text("Rahmat! Siz barcha kanallarga obuna bo‘lgansiz. Botdan foydalanishingiz mumkin.")
    else:
        await call.answer("Siz hali ham barcha kanallarga obuna bo‘lmagansiz!", show_alert=True)




# @dp.message(F.video | F.photo | F.document | F.audio | F.voice)
# async def get_file_id(message: types.Message):
    
#     user_id = message.from_user.id
#     if await check_subs(user_id):
#         if message.video:
#             await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
#     else:
#         await message.answer('telegram kanalga obuna boling')



@dp.message(F.video | F.photo | F.document | F.audio | F.voice)
async def get_file_id(message: types.Message):
    user_id = message.from_user.id

    # Faqat adminlarga ruxsat beramiz
    if user_id in ADMINS:
        if message.video:
            await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
        elif message.photo:
            await message.answer(f"🖼 Photo File ID: `{message.photo[-1].file_id}`")
        elif message.document:
            await message.answer(f"📄 Document File ID: `{message.document.file_id}`")
        elif message.audio:
            await message.answer(f"🎵 Audio File ID: `{message.audio.file_id}`")
        elif message.voice:
            await message.answer(f"🎙 Voice File ID: `{message.voice.file_id}`")
    else:
        await message.answer("🚫 Ushbu buyruq faqat adminlar uchun mavjud!")

@dp.message(F.text == "1") #buyerga kino kodi kiritiladi
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAN_aNAEDQ_iEux5ZWFg36iiPbqk-GAAAqMSAAK066BKRsdVZQAB4qmgNgQ" #buyerga kino id kiritiladi
        await message.answer_video(file_id, caption="🎬  Mening yigitim zombi") #buyerga kino nomi kiritiladi
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)







# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "2")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAOxaNS-JLwYHlk_BtOjqJhZ58SvqxIAAuMKAAK-hqFKHs6_Ih9v0qI2BA"
        await message.answer_video(file_id, caption="Favqulotda qongiroq")
                                                        
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "45")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAMkaM_LTITXUe-QO7uQLV9RveS8a2wAAsd_AAKeD8lJmUuS3jkgBMY2BA"
        await message.answer_video(file_id, caption="""🏷️Anime nomi: Log harizon
🖋️Janri: Drama, Fantastika, Sarguzash
🎞️ Qismlar soni: 12
🎙️ Ovoz berdi: @uchiha_fandubbing
💭 Tili: Uzbek
Bu Log harizonni 4-qismi 
Uzbek tilida 😁""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)





@dp.message(F.text == "50")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAM0aM_NLRpb-W_2Ao_6mnMjK4AaMggAAkOAAAI5D2lKPGY2pfNr2LE2BA"
        await message.answer_video(file_id, caption="""«Yaxshi yigit» 4-qism [360p]""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)







async def main():
    print('bot ishladi....')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())









