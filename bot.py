from aiogram import Bot, Dispatcher, types,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import asyncio

TOKEN = "8429983629:AAFyk9p5fS4M4G8i5HGdDqbeiRNBCzaoN_g"
CHANNELS = ["@Tarjima_kinolar_uzb_tilda_z"]  # Majburiy obuna kanallari
ADMINS = [6000119173]
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Kanallardagi jami obunachilar sonini hisoblaydi (faqat adminlar ko‘radi)
async def get_subs_count():
    total = 0
    for channel in CHANNELS:
        count = await bot.get_chat_member_count(channel)  # aiogram v3 da to‘g‘ri metod
        total += count
    return total


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
        text = "Xush kelibsiz! Botdan foydalanishingiz mumkin."
        if user_id in ADMINS:  # faqat adminlar uchun
            subs_count = await get_subs_count()
            text += f"\n📊 Jami obunachilar soni: {subs_count}"
        await message.answer(text)

@dp.callback_query(lambda call: call.data == "check_subs")
async def check_subs_callback(call: types.CallbackQuery):
    user_id = call.from_user.id
    if await check_subs(user_id):
        text = "Rahmat! Siz barcha kanallarga obuna bo‘lgansiz."
        if user_id in ADMINS:  # faqat adminlar uchun
            subs_count = await get_subs_count()
            text += f"\n📊 Jami obunachilar soni: {subs_count}"
        await call.message.edit_text(text)
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
        file_id = "BAACAgQAAxkBAAIB7mjffyMGjHamuD2gWpH5dySLil2vAALnFwACI-6BUBpd5hYmbW6NNgQ" #buyerga kino id kiritiladi
        await message.answer_video(file_id, caption="""🎬  🎥 Mening yigitim zombi
📹 Sifati: HD 720p
📆 Yil: 2013
🎞 Janr: Komediya Triller 
🇺🇸 Davlat: AQSH
🇺🇿 Tarjima: O'zbek tilida
🗂 Yuklash: 1028""") #buyerga kino nomi kiritiladi
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


@dp.message(F.text == "3")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAOoaNAkfAxgMB-mjbTUr9fGLGeOTcgAAh0PAAJS5vFIXwwVOys71a02BA"
        await message.answer_video(file_id, caption="""Biz hayvonot bog'ini sotib oldik""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)





@dp.message(F.text == "4")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAO6aNTAuD-P1hkRT54xuNTk2bSw6iUAAhIaAAJqt6FLacWssGdHT242BA"
        await message.answer_video(file_id, caption="""Qo'lingdan Kelsa Tutib Ol [1080p]""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "5")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPLaN06iR9GYw9F0_uTnpByk8Rsa4cAAsENAALrJiBJoLM4cqeecKE2BA"
        await message.answer_video(file_id, caption="""Kino nomi;Fath[1080p]""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "6")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPQaN1VrnDvEYo54rRqJCUZbRVN9ZkAAllPAAK-9NFJx-y63-ouTA42BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «172 kun» to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 6

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "7")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPTaN1XMwqZe--ck5ImMyitrp9FsW4AAltUAAKIXghJPkDy0sG2Ymc2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: Jannat onalar oyog'i ostida to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 7

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "8")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPXaN1YgFVyf2HE646zmiOMHi07-i0AAuJUAAILRMhI0DiVpjJPiSk2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «Jannat rangi» to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 8

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



@dp.message(F.text == "9")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPZaN1ZAAGFRzMf6Y1Vh1fEeRfc8YrJAAIULAACR8ugS4DttSPq1kxWNgQ"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: «Iftorlik suvi»  to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2024-08-18
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 9

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "10")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAPvaN4NzWOZiaRpOCHpmYk3ARpDpZEAAoQUAAK4jfFKzLNPlW34YNY2BA"
        await message.answer_video(file_id, caption="""🍿 Kino nomi: << Muqaddas Zamin>> to'liq kino

🇺🇿 O'zbek tilida

📅 Yuklangan sanasi: 2025-10-02
sifati; [1080p]
🗂 Yuklash: 8660

🔎 Kinoning kodi: 10

‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "11")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICF2jfldbQq1IqAdigYvruuqwU0rleAALQIAACoARRSJ0H__nIiycUNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 1-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



@dp.message(F.text == "12")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICGWjflp780Dw0cbzBToZ20mpcPRMNAAL1AgAC8uNZRK73OyHZ65ydNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 2-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "13")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICG2jfluaUfww1gzRRhzvM3F5zYDA8AAIOJAACMSdwSJubOHSzH-4GNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 3-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "14")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICHWjflx8SgbJqL1A-94bD1QF43r8tAAIYEAACDD2BUCKbrJhB7G-kNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 4-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "15")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICH2jfl2Ff9v9JHyT5TnQLVtWAYu92AAJuDwACDD2JUB5lmH-5obvPNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 5-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "16")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICIWjfl5AnUoQw6bbALwpRF8-nnq5BAAK5DQACN5mgUFOvXwOGhXsQNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 6-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "17")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICI2jfl-gCVEqDUKQwAAE3yGRylUQQcwACqQ8AAmaMqVCQPTGFg7eIZTYE"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 7-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "18")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICJWjfmBybTIIcGaJevMeZxrN9o87rAAJiAgACtAaxRDu0zQvmUR8wNgQ"
        await message.answer_video(file_id, caption="""1-Fasl.
Wendesday 8-Qism
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "19")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICN2jfmQyhmGg8kLvaY7s4nTdeq0DFAAKyGQAC9QGhUA_2YnUomY6jNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 1-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "20")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICOWjfmTk8MnxZ-MVf3pKkbXsJat17AALnGQAC9QGhUPIj54jrtNipNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 2-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "21")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICO2jfmWvj839-qmE7NZYYJRSzI9dqAAKrewAC-4egSKUecVSwGtRgNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 3-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "22")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICPWjfmZ83DnC9uO1I3rmhwxY1-SWNAALIewAC-4egSGPXPzY7_PBONgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 4-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "23")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAICP2jfmdDOxuPZOJ-bQykIEPeXKQOuAAJlHAACJ1XAUf2_Uom-Cj5KNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 5-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "24")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICQWjfmgF2-N9cHw_auHYVSNT_DZAnAAKchgAChKnBSZ5IbXfph-arNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 6-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "25")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICQ2jfmi9VyJ_m1RajSobEHj3mPAkrAAKHggAChBnJSSZAiewXWh_XNgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 7-qism
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "26")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAICRWjfmmuRYxBnyKS-HmpieYdsS6wIAAIGgwAChBnJSe-G2itus1-2NgQ"
        await message.answer_video(file_id, caption="""Wednesday 2-fasl 8-qism ( final )
• Oʻzbek tilida (Uzmovi tarjimasi)
• #fantaziya #maktab #komedia #triller
• Mobile HD Kesilmagan Orginal
• Sifat: 480p
‼️Serial bo'lsa, Keyingi qismini ko'rish uchun, keyingi sonni yozasiz.""")
    else:
        await message.answer('telegram kanalga obuna boling')
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)



# 📌 2️⃣ Xabar "2" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "27")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAICWmjfomdEIJm9RBHwMfMOihVrLygdAAL3AwAC6SvJRoiAhKj_Di2ZNgQ"
        await message.answer_video(file_id, caption="""⌨️ KOD: #27  
       bot; @UrtakKino_bot
        kanal; @Tarjima_kinolar_uzb_tilda_z""")
                                                        
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

