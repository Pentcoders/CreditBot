import logging
from config import API_Token
import msg as m
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_Token)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await bot.send_photo(message.chat.id, open('image/start.jpg', 'rb'), caption=m.start_msg, reply_markup=kb.menubut)
	#await message.answer(m.start_msg, reply_markup=kb.menubut)


@dp.message_handler(content_types=['text'])
async def h(message: types.Message, state: FSMContext):
	await message.answer(m.xz)

@dp.callback_query_handler(lambda call: True)
async def cal(call, state: FSMContext):
	if 'docopen' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/potribit.jpg', 'rb'))
		await call.message.answer(m.opendoc, reply_markup=kb.docopen)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'credit' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/avtocredit.jpg', 'rb'))
		#await bot.send_animation(chat_id, open('image/two.gif', 'rb'), caption=m.credit, reply_markup=kb.credit)
		await call.message.answer(m.credit, reply_markup=kb.credit)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ipoteka' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/moneyzlogip.jpg', 'rb'), caption=m.ipoteka, reply_markup=kb.ipoteka)
		#await bot.send_animation(chat_id, open('image/two.gif', 'rb'), caption=m.ipoteka, reply_markup=kb.ipoteka)
		#await call.message.answer(m.ipoteka, reply_markup=kb.ipoteka)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'checkCS' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/checkks.jpg', 'rb'), caption=m.checkCS, reply_markup=kb.checkCS)
		#await call.message.answer(m.checkCS, reply_markup=kb.checkCS)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ogotovz' in call.data:
		await call.message.answer(m.ogotovz, reply_markup=kb.ogotovz)
		await bot.delete_message(call.message.chat.id, call.message.message_id)

	elif 'moneyned' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/moneyzlogip.jpg', 'rb'))
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'nepodxod' in call.data:
		await call.message.answer(m.nepodxod, reply_markup=kb.nepodxod)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'garantii' in call.data:
		await call.message.answer(m.garantii, reply_markup=kb.garantii)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'fizlic' in call.data:
		await call.message.answer(m.fizlic, reply_markup=kb.fizlic)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'checkOKB' in call.data:
		await call.message.answer(m.checkOKB, reply_markup=kb.checkOKB)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'samofree' in call.data:
		await call.message.answer(m.samofree, reply_markup=kb.samofree)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'spravkigot' in call.data:
		await call.message.answer(m.spravkigot, reply_markup=kb.spravkigot)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'yulic' in call.data:
		await call.message.answer(m.yulic, reply_markup=kb.yulic)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ip' in call.data:
		await call.message.answer(m.ip, reply_markup=kb.ip)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'sootv' in call.data:
		await call.message.answer(m.sootv, reply_markup=kb.sootv)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'yesgotov' in call.data:
		await call.message.answer(m.yesgotov, reply_markup=kb.yesgotov)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'nesootv' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/start.jpg', 'rb'), caption=m.start_msg, reply_markup=kb.menubut)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ooo' in call.data:
		await call.message.answer(m.ooo, reply_markup=kb.ooo)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'coo' in call.data:
		await call.message.answer(m.coo, reply_markup=kb.coo)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'needcon' in call.data:
		await call.message.answer(m.needcon, reply_markup=kb.needcon)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'needIB' in call.data:
		await call.message.answer(m.needIB, reply_markup=kb.needIB)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'alldocgat' in call.data:
		await call.message.answer(m.alldocgat, reply_markup=kb.alldocgat)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'stdialog' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('image/start.jpg', 'rb'), caption=m.start_msg, reply_markup=kb.menubut)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ready' in call.data:
		await call.message.answer(m.ready, reply_markup=kb.ready)
		await bot.delete_message(call.message.chat.id, call.message.message_id)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)