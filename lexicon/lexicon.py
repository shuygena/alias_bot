LEXICON = { '/start': """<b>Привет!</b>
Чтобы вспомнить правила игры воспользуйся командой /rules

Настройки по умолчанию
Язык: <b>Русский</b> 🇷🇺
Уровень сложности: <b>Нормальный</b> 🥈
Длительность раунда: <b>60 секунд</b> ⏱
Требуется очков для победы: <b>100</b> 💯
За пропущенные слова очки: <b>не отнимаются</b> ⏭
Последнее слово отгадывать по истечению таймера: <b>нельзя</b> ❌
О том, как поменять настройки читай в /help

<b>Чтобы начать новую игру нажми на кнопку под этим сообщением или напиши команду /game </b>""",

'/help': """Начать новую игру - /game
Вспомнить правила игры - /rules
Информация о текущей игре - /info

Изменить настройки игры:
/set_language - Изменить язык
/set_level - Изменить уровень сложности
/set_score_to_win - Изменить количество очков, требуемых для победы (максимум до 200)
/set_time - Изменить длительность раунда 
/set_pass_tax - Рассчёт очков за пропущенные слова
/reset

Связаться с автором бота: @mskeleto""",

'/game': """Отлично 🙌
Для начала зарегистрируй команды.
Для этого пришли сообщение с названиями команд. Каждое название пиши в новой строке.

<b>Например:</b>
Три шакала
Совунья и пельмени""",

'/rules': """<b>Правила игры:</b>

1. Расшифровка слова должна осуществляться без его прямого упоминания и использования однокоренных слов.

2. Запрещено использовать перевод слова на иностранные языки.

3. Когда отгадана часть словосочетания, то ее можно использовать в дальнейших объяснениях.

4. Использование как синонимов, так и антонимов загаданных слов разрешено.

5.  Важно, чтобы команда при отгадывании уложилась в определенные временные рамки.

6. Каждая команда должна отыграть раунд. Из всех команд, преодолевших необходимый для выигрыша порог, побеждает та, у которой больше всего очков.""",

'not_names': """Пожалуйста, введи названия команд: каждое название пиши в новой строке.
Учти, что в игре может участвовать не больше 4 команд!""",
'use_buttons': "Пожалуйста, для выбора настроек воспользуйся кнопками 👆",

'/set_time' : """ message too long""",
'/set_language' : """Выбери язык с помощью кнопок. Ниже приведена информация в формате:
Язык: слова на лёгкий/нормальный/сложный уровень

<b>Русский</b>: 2050/3106/2410 слов 
<b>Английский</b>: 2108/3981/4695 слов
<b>Карачаево-балкарский</b>: В ПРОЦЕССЕ формирования словарей""",
'/set_level': """Выбери уровень с помощью кнопок:
""",
'/set_pass_tax': "Отнимать очки за пропущенные слова?",
'/set_time': """Введи желательную длительность раунда в секундах от 10 до 300.
Напоминаем, что в одной минуте 60 секунд."""
}
