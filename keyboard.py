from aiogram import types


menubut = types.InlineKeyboardMarkup(row_width=1)
menubut.add(
	types.InlineKeyboardButton(text='1. Потрибительский кредит', callback_data='docopen'),
	types.InlineKeyboardButton(text='2. Ипотека', callback_data='ipoteka'),
	types.InlineKeyboardButton(text='3. Авто кредит', callback_data='credit'),
	types.InlineKeyboardButton(text='4. Деньги под залог недвижимости', callback_data='moneyned'),
	types.InlineKeyboardButton(text='5. Проверка кредитной истории', callback_data='checkCS'),
	#types.InlineKeyboardButton(text='5. Доступ в закрытый канал', url='https://t.me/assistant_credit_bot'),
	)

docopen = types.InlineKeyboardMarkup(row_width=1)
docopen.add(
	types.InlineKeyboardButton(text='Отлично! Готов заказать.', callback_data='ogotovz'),
	types.InlineKeyboardButton(text='Такие условия мне не подходят', callback_data='nepodxod'),
	types.InlineKeyboardButton(text='А какие гарантии?', callback_data='garantii'),
)

docopen = types.InlineKeyboardMarkup(row_width=1)
docopen.add(
	types.InlineKeyboardButton(text='Есть еще вопросы. Связь с специалистом', url='https://t.me/kredit_assistant'),
	types.InlineKeyboardButton(text='Хорошо. Готов заказать.', callback_data='ogotovz'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),

	)

ogotovz = types.InlineKeyboardMarkup(row_width=1)
ogotovz.add(
	types.InlineKeyboardButton(text='Помощь. (связь с специалистом)', url='https://t.me/kredit_assistant'),
	)

nepodxod = types.InlineKeyboardMarkup(row_width=1)
nepodxod.add(
	types.InlineKeyboardButton(text='Начать диалог с ботом заново.', callback_data='stdialog'),

	)

credit = types.InlineKeyboardMarkup(row_width=1)
credit.add(
	types.InlineKeyboardButton(text='Физическое лицо', callback_data='fizlic'),
	types.InlineKeyboardButton(text='Юридическое лицо', callback_data='yulic'),
	)

yulic = types.InlineKeyboardMarkup(row_width=1)
yulic.add(
	types.InlineKeyboardButton(text='ИП', callback_data='ip'),
	types.InlineKeyboardButton(text='ООО', callback_data='ooo'),
	types.InlineKeyboardButton(text='Условия мне не подходят', callback_data='nepodxod'),
	)

ooo = types.InlineKeyboardMarkup(row_width=1)
ooo.add(
	types.InlineKeyboardButton(text='ООО соответствует данным требованиям', callback_data='coo'),
	types.InlineKeyboardButton(text='ООО не соответствует данным требованиям', callback_data='stdialog'),
	)

coo = types.InlineKeyboardMarkup(row_width=1)
coo.add(
	types.InlineKeyboardButton(text='Да, у меня все готово.', callback_data='yesgotov'),
	types.InlineKeyboardButton(text='Не готов сейчас подавать документы.', callback_data='stdialog'),
	types.InlineKeyboardButton(text='Проверить ОКБ, НБКИ', callback_data='checkOKB'),
	types.InlineKeyboardButton(text='Написать специалисту', url='https://t.me/kredit_assistant'),
	
	)


ip = types.InlineKeyboardMarkup(row_width=1)
ip.add(
	types.InlineKeyboardButton(text='ИП соответствует данным требованиям', callback_data='sootv'),
	types.InlineKeyboardButton(text='ИП не соответствует данным требованиям', callback_data='stdialog'),
	)

sootv = types.InlineKeyboardMarkup(row_width=1)
sootv.add(
	types.InlineKeyboardButton(text='Да, у меня все готово.', callback_data='yesgotov'),
	types.InlineKeyboardButton(text='Не готов сейчас подавать документы.', callback_data='stdialog'),
	types.InlineKeyboardButton(text='Проверить ОКБ, НБКИ', callback_data='checkOKB'),
	)

fizlic = types.InlineKeyboardMarkup(row_width=1)
fizlic.add(
	types.InlineKeyboardButton(text='Условия устраивают. Заполнить анкету', callback_data='ogotovz'),
	types.InlineKeyboardButton(text='Нет, мне это не подходит', callback_data='nepodxod'),
	types.InlineKeyboardButton(text='Проверить ОКБ, НБКИ', callback_data='checkOKB'),
	)

checkOKB = types.InlineKeyboardMarkup(row_width=1)
checkOKB.add(
	types.InlineKeyboardButton(text='Самостоятельно проверю кредитную историю', callback_data='samofree'),
	types.InlineKeyboardButton(text='Готов оплатить услугу', callback_data='ready'),

	)

yesgotov = types.InlineKeyboardMarkup(row_width=1)
yesgotov.add(
	types.InlineKeyboardButton(text='Написать специалисту', url='https://t.me/kredit_assistant'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),

	)

samofree = types.InlineKeyboardMarkup(row_width=1)
samofree.add(
	types.InlineKeyboardButton(text='Справки из ОКБ, НБКИ готовы!', callback_data='spravkigot'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),

	)

spravkigot = types.InlineKeyboardMarkup(row_width=1)
spravkigot.add(
	types.InlineKeyboardButton(text='Связаться с специалистом для анализов документов', url='https://t.me/kredit_assistant'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),

	)

ipoteka = types.InlineKeyboardMarkup(row_width=1)
ipoteka.add(
	types.InlineKeyboardButton(text='Помогите проверить мою кредитную историю', callback_data='checkOKB'),
	types.InlineKeyboardButton(text='Нужна консультация специалиста', callback_data='needcon'),
	types.InlineKeyboardButton(text='Нужен ипотечный брокер', callback_data='needIB'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),
	)

checkCS = types.InlineKeyboardMarkup(row_width=1)
checkCS.add(
	types.InlineKeyboardButton(text='Готов оплатить', callback_data='ready'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),

	)

needcon = types.InlineKeyboardMarkup(row_width=1)
needcon.add(
	types.InlineKeyboardButton(text='Нужна помощь, связаться с специалистом', url='https://t.me/kredit_assistant'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),
	types.InlineKeyboardButton(text='Я все оплатил, вязаться с специалистом ', url='https://t.me/kredit_assistant'),

	)

needIB = types.InlineKeyboardMarkup(row_width=1)
needIB.add(
	types.InlineKeyboardButton(text='Все документы собраны', callback_data='alldocgat'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),
	types.InlineKeyboardButton(text='Проверить ОКБ, НБКИ', callback_data='checkOKB'),

	)

alldocgat = types.InlineKeyboardMarkup(row_width=1)
alldocgat.add(
	types.InlineKeyboardButton(text='Готов оплатить', callback_data='ready'),
	types.InlineKeyboardButton(text='Начать диалог с ботом заново', callback_data='stdialog'),
	types.InlineKeyboardButton(text='Cвязаться с специалистом', url='https://t.me/kredit_assistant'),

	)

ready = types.InlineKeyboardMarkup(row_width=1)
ready.add(
	types.InlineKeyboardButton(text='Я все оплатил, вязаться с специалистом ', url='https://t.me/kredit_assistant'),
	types.InlineKeyboardButton(text='Не готов оплачивать', callback_data='stdialog'),
	)