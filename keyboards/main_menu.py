from aiogram import Dispatcher, types


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/game', description='Начать игру'),
        types.BotCommand(command='/rules', description='Правила игры'),
        types.BotCommand(command='/help', description='help'),
        types.BotCommand(command='/set_language', description='Изменить язык'),
        types.BotCommand(command='/set_level', description='Изменить уровень сложности'),
        types.BotCommand(command='/set_points', description='Изменить условие победы'),
        types.BotCommand(command='/set_time', description='Изменить длительность раунда'),
        types.BotCommand(command='/set_pass_tax', description='Рассчёт пропущенных строк')
        # Последнее слово объяснять сколько хочешь
        # Изменить название команды
        # Остановить игру
        # Перезапустить игру
    ]
    await dp.bot.set_my_commands(main_menu_commands)