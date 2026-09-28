import asyncio

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

from loader import bot, db, db2
from data.config import ADMINS, ADMIN_PASSWORD
from states.adminState import AdminState
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from keyboards.default.adminkeyboards import Adminkeyboard

admin_router = Router()


def _stats_text():
    users = db.count_users()[0]
    try:
        msgs = db2.count_messages()[0]
    except Exception:
        msgs = 0
    return f"📊 Statistika\n\n👥 Foydalanuvchilar: <b>{users}</b>\n✉️ Fikr-xabarlar: <b>{msgs}</b>"


@admin_router.message(Command("admin"), F.from_user.id.in_(ADMINS), StateFilter("*"))
async def ask_password(message: Message, state: FSMContext):
    await message.answer("🔐 Parolni kiriting:", reply_markup=mainMenuKeyboard)
    await state.set_state(AdminState.parol)


@admin_router.message(AdminState.parol, F.from_user.id.in_(ADMINS), F.text == ADMIN_PASSWORD)
async def open_panel(message: Message, state: FSMContext):
    try:
        await message.delete()
    except Exception:
        pass
    await message.answer("🛠 <b>Admin panel</b>\n\n" + _stats_text(), reply_markup=Adminkeyboard)
    await state.set_state(AdminState.admin)


@admin_router.message(AdminState.parol, F.from_user.id.in_(ADMINS))
async def wrong_password(message: Message):
    a = await message.answer("❌ Parol noto'g'ri")
    await asyncio.sleep(2)
    try:
        await message.delete()
        await a.delete()
    except Exception:
        pass


@admin_router.message(AdminState.admin, F.text == "📊 Statistika")
async def stats(message: Message):
    await message.answer(_stats_text())


@admin_router.message(AdminState.admin, F.text.in_({"📥 Foydalanuvchilar", "/allusers"}))
async def all_users(message: Message):
    users = db.select_all_users()
    await message.answer(f"Bazada {len(users)} ta foydalanuvchi bor.")
    with open('users.txt', 'w', encoding="utf-8") as file:
        file.write(str(users))
    await message.answer_document(FSInputFile('users.txt'))
    try:
        await message.answer_document(FSInputFile('data/main.db'))
    except Exception:
        pass


@admin_router.message(AdminState.admin, F.text.in_({"✅ Tekshirish", "/checkusers"}))
async def check_users(message: Message):
    status = await message.answer("⏳ Tekshirilmoqda...")
    users = db.select_all_users()
    sended = unsended = 0
    for user in users:
        try:
            await bot.send_chat_action(chat_id=user[0], action="typing")
            sended += 1
            await asyncio.sleep(0.05)
        except Exception:
            unsended += 1
    await status.edit_text(f"✅ Aktiv: <b>{sended}</b>\n🚫 O'chirgan/bloklagan: <b>{unsended}</b>")


# --- Reklama (tasdiqlash bilan) ---
@admin_router.message(AdminState.admin, F.text.in_({"📢 Reklama", "/reklama"}))
async def ask_ad(message: Message, state: FSMContext):
    await message.answer("📢 Tarqatiladigan xabarni yuboring (matn, rasm, video — istalgani):",
                         reply_markup=mainMenuKeyboard)
    await state.set_state(AdminState.reklama)


@admin_router.message(AdminState.reklama)
async def preview_ad(message: Message, state: FSMContext):
    await state.update_data(ad_chat=message.chat.id, ad_msg=message.message_id)
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Yuborish", callback_data="adm_send"),
        InlineKeyboardButton(text="❌ Bekor", callback_data="adm_cancel"),
    ]])
    await message.answer("👆 Shu xabar barcha foydalanuvchilarga yuboriladi. Tasdiqlaysizmi?", reply_markup=kb)


@admin_router.callback_query(F.data == "adm_cancel", F.from_user.id.in_(ADMINS))
async def ad_cancel(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("❌ Bekor qilindi.")
    await state.set_state(AdminState.admin)
    await call.answer()


@admin_router.callback_query(F.data == "adm_send", F.from_user.id.in_(ADMINS))
async def ad_send(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    ad_chat, ad_msg = data.get("ad_chat"), data.get("ad_msg")
    if not ad_chat:
        await call.answer("Xabar topilmadi", show_alert=True)
        return
    await call.message.edit_text("📤 Yuborilmoqda...")
    users = db.select_all_users()
    sended = unsended = 0
    for i, user in enumerate(users, 1):
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=ad_chat, message_id=ad_msg)
            sended += 1
            await asyncio.sleep(0.05)
        except Exception:
            unsended += 1
        if i % 25 == 0:
            try:
                await call.message.edit_text(f"📤 {i}/{len(users)}... (✅ {sended} / 🚫 {unsended})")
            except Exception:
                pass
    await call.message.edit_text(f"✅ Yakunlandi.\nYuborildi: <b>{sended}</b>\nYuborilmadi: <b>{unsended}</b>")
    await state.set_state(AdminState.admin)
    await call.answer()


# --- Bazani tozalash (tasdiqlash bilan) ---
@admin_router.message(AdminState.admin, F.text.in_({"🗑 Bazani tozalash", "/cleandb"}))
async def ask_clean(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🗑 Ha, tozalash", callback_data="adm_clean_yes"),
        InlineKeyboardButton(text="❌ Yo'q", callback_data="adm_clean_no"),
    ]])
    await message.answer("⚠️ Diqqat! Barcha foydalanuvchilar bazadan o'chiriladi. Davom etamizmi?", reply_markup=kb)


@admin_router.callback_query(F.data == "adm_clean_no", F.from_user.id.in_(ADMINS))
async def clean_no(call: CallbackQuery):
    await call.message.edit_text("❌ Bekor qilindi.")
    await call.answer()


@admin_router.callback_query(F.data == "adm_clean_yes", F.from_user.id.in_(ADMINS))
async def clean_yes(call: CallbackQuery):
    db.delete_users()
    await call.message.edit_text("🗑 Baza tozalandi!")
    await call.answer()
