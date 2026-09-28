import asyncio

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from loader import bot, db
from data.config import ADMINS
from states.adminState import AdminState
from keyboards.default.mainMenuKeyboard import mainMenuKeyboard
from keyboards.default.adminkeyboards import Adminkeyboard

admin_router = Router()

PASSWORD = "rtwgjmja"  # TODO: .env fayliga ko'chirish tavsiya etiladi


@admin_router.message(Command("admin"), F.from_user.id.in_(ADMINS), StateFilter("*"))
async def ask_password(message: Message, state: FSMContext):
    await message.answer("parolni kiriting", reply_markup=mainMenuKeyboard)
    await state.set_state(AdminState.parol)


@admin_router.message(AdminState.parol, F.from_user.id.in_(ADMINS), F.text == PASSWORD)
async def open_panel(message: Message, state: FSMContext):
    await message.delete()
    await message.answer(
        "Admin panel\n\nAdmin komandalar\n"
        "/allusers - bazadagi obunachilar soni, txt va db fayllari\n"
        "/checkusers - botdagi faol va o'chirilgan akkauntlar sonini aniqlash\n"
        "/reklama - reklama tarqatish\n"
        "/cleandb - bazani tozalash",
        reply_markup=Adminkeyboard,
    )
    await state.set_state(AdminState.admin)


@admin_router.message(AdminState.parol, F.from_user.id.in_(ADMINS))
async def wrong_password(message: Message):
    a = await message.answer("parol nato'g'ri")
    await asyncio.sleep(2)
    try:
        await message.delete()
        await a.delete()
    except Exception:
        pass


@admin_router.message(AdminState.admin, F.text.in_({"Allusers", "/allusers"}))
async def all_users(message: Message):
    users = db.select_all_users()
    await message.answer(f"Bazada {len(users)} ta foydalanuvchi bor.")
    with open('users.txt', 'w', encoding="utf-8") as file:
        file.write(str(users))
    await message.answer_document(FSInputFile('users.txt'))
    await message.answer_document(FSInputFile('data/main.db'))


@admin_router.message(AdminState.admin, F.text.in_({"Check users", "/checkusers"}))
async def check_users(message: Message):
    await message.answer("Tekshirish boshlandi")
    users = db.select_all_users()
    sended = unsended = 0
    for user in users:
        try:
            await bot.send_chat_action(chat_id=user[0], action="typing")
            sended += 1
            await asyncio.sleep(0.05)
        except Exception:
            unsended += 1
    await message.answer(
        f"{sended} ta foydalanuvchi aktiv. {unsended} ta foydalanuvchi o'chirilgan."
    )


@admin_router.message(AdminState.admin, F.text.in_({"/reklama", "Reklama"}))
async def ask_ad(message: Message, state: FSMContext):
    await message.answer('reklama yuboring', reply_markup=mainMenuKeyboard)
    await state.set_state(AdminState.reklama)


@admin_router.message(AdminState.reklama)
async def send_ad(message: Message, state: FSMContext):
    users = db.select_all_users()
    sended = unsended = 0
    for user in users:
        try:
            await message.send_copy(chat_id=user[0])
            sended += 1
            await asyncio.sleep(0.05)
        except Exception:
            unsended += 1
    await message.answer(
        f"reklama {sended} ta odamga yuborildi, {unsended} ta odamga yuborib bo'lmadi",
        reply_markup=Adminkeyboard,
    )
    await state.set_state(AdminState.admin)


@admin_router.message(AdminState.admin, F.text == "/cleandb")
async def clean_db(message: Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
