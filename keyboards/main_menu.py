from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Запустить бота'),
        types.BotCommand(command='/game', description='Начать игру'),
        types.BotCommand(command='/rules', description='Правила игры'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/info', description='Информация о текущей игре'),
        types.BotCommand(command='/set_language', description='Изменить язык'),
        types.BotCommand(command='/set_level', description='Изменить уровень сложности'),
        types.BotCommand(command='/set_score_to_win', description='Изменить счет победы'),
        types.BotCommand(command='/set_time', description='Изменить длительность раунда'),
        types.BotCommand(command='/set_pass_tax', description='Рассчёт пропущенных слов'),
        types.BotCommand(command='/reset', description='Сбросить настройки')
    ]
    await dp.bot.set_my_commands(main_menu_commands)