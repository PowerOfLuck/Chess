from tkinter import *
from PIL import Image, ImageTk


def check_shah(new_key, base, new_value, old_key, old_value, init, Base_Mechanic):

    # Условная переменная,
    # первое значение при изменении останавливает код,
    # второе создает белого ферзя, третье черного (для пешек на 8-1 полях)
    available_moovs = {}

    # [6] = y
    # [7] = x
    if old_value[8] in init.black_types:

        # ********** ПЕШКА **************
        if old_value[8] == 'Black_Pawn':

            # Создание списка доступных ходов
            for key, value in base.items():
                # Взятие фигур
                if value[6] == old_value[6] - 1 and value[7] == old_value[7] + 1:
                    available_moovs[key] = value
                elif value[6] == old_value[6] - 1 and value[7] == old_value[7] - 1:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** КОНЬ **************
        elif old_value[8] == 'Black_Knight':

            for key, value in base.items():
                # Легендарная формула просчета движения коня
                if old_value[6] - 2 == value[6] and old_value[7] - 1 == value[7] or \
                        old_value[6] - 2 == value[6] and old_value[7] + 1 == value[7] or \
                        old_value[6] - 1 == value[6] and old_value[7] + 2 == value[7] or \
                        old_value[6] + 1 == value[6] and old_value[7] + 2 == value[7] or \
                        old_value[6] + 2 == value[6] and old_value[7] + 1 == value[7] or \
                        old_value[6] - 1 == value[6] and old_value[7] - 2 == value[7] or \
                        old_value[6] + 2 == value[6] and old_value[7] - 1 == value[7] or \
                        old_value[6] + 1 == value[6] and old_value[7] - 2 == value[7] or \
                        old_value[6] - 2 == value[6] and old_value[7] - 1 == value[7]:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** СЛОН **************
        elif old_value[8] == 'Black_Officer':

            for key, value in base.items():
                if ((old_value[6] - value[6]) == (old_value[7] - value[7]) or
                    (value[6] - old_value[6]) == (old_value[7] - value[7])) and not (
                        old_value[6] == value[6] and old_value[7] == value[7]):
                    # Сбор значений с двух диагоналей
                    available_moovs[key] = value


            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs

        # ********** ЛАДЬЯ **************
        elif old_value[8] == 'Black_Rook':

            for key, value in base.items():
                if old_value[6] != value[6] and old_value[7] == value[7]:
                    available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs

        # ********** ФЕРЗЬ **************
        elif old_value[8] == 'Black_Queen':

            for key, value in base.items():

                if ((old_value[6] - value[6]) == (old_value[7] - value[7]) or
                    (value[6] - old_value[6]) == (old_value[7] - value[7])) and not (
                        old_value[6] == value[6] and old_value[7] == value[7]):

                    # Сбор значений с двух диагоналей
                    available_moovs[key] = value

                elif old_value[6] != value[6] and old_value[7] == value[7]:
                    available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    available_moovs[key] = value


            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]

            available_moovs = temp_available_moovs

        # ********** КОРОЛЬ **************
        elif old_value[8] == 'Black_King':

            for key, value in base.items():
                if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                        old_value[7] - value[7]):
                    if old_value[6] - value[6] == 1 or old_value[6] - value[6] == -1:
                        # Сбор значений с двух диагоналей
                        available_moovs[key] = value

                elif old_value[6] != value[6] and old_value[7] == value[7]:
                    if old_value[6] - value[6] == 1 or old_value[6] - value[6] == -1:
                        available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    if old_value[7] - value[7] == 1 or old_value[7] - value[7] == -1:
                        available_moovs[key] = value



        return available_moovs


    if old_value[8] in init.white_types:

        available_moovs = {}

        # ********** ПЕШКА **************
        if old_value[8] == 'Wight_Pawn':
            # Создание списка доступных ходов
            for key, value in base.items():
                # Взятие фигур
                if value[6] == old_value[6] + 1 and value[7] == old_value[7] + 1:
                    available_moovs[key] = value
                elif value[6] == old_value[6] + 1 and value[7] == old_value[7] - 1:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** КОНЬ **************
        elif old_value[8] == 'Wight_Knight':

            for key, value in base.items():
                # Легендарная формула просчета движения коня
                if old_value[6] - 2 == value[6] and old_value[7] - 1 == value[7] or \
                        old_value[6] - 2 == value[6] and old_value[7] + 1 == value[7] or \
                        old_value[6] - 1 == value[6] and old_value[7] + 2 == value[7] or \
                        old_value[6] + 1 == value[6] and old_value[7] + 2 == value[7] or \
                        old_value[6] + 2 == value[6] and old_value[7] + 1 == value[7] or \
                        old_value[6] - 1 == value[6] and old_value[7] - 2 == value[7] or \
                        old_value[6] + 2 == value[6] and old_value[7] - 1 == value[7] or \
                        old_value[6] + 1 == value[6] and old_value[7] - 2 == value[7] or \
                        old_value[6] - 2 == value[6] and old_value[7] - 1 == value[7]:
                    available_moovs[key] = value
            # Копия словаря
            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** СЛОН **************
        elif old_value[8] == 'Wight_Officer':

            for key, value in base.items():
                if ((old_value[6] - value[6]) == (old_value[7] - value[7]) or
                    (value[6] - old_value[6]) == (old_value[7] - value[7])) and not (
                        old_value[6] == value[6] and old_value[7] == value[7]):
                    # Сбор значений с двух диагоналей
                    available_moovs[key] = value


            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** ЛАДЬЯ **************
        elif old_value[8] == 'Wight_Rook':

            for key, value in base.items():
                if old_value[6] != value[6] and old_value[7] == value[7]:
                    available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]
            available_moovs = temp_available_moovs


        # ********** ФЕРЗЬ **************
        elif old_value[8] == 'Wight_Queen':

            for key, value in base.items():
                if ((old_value[6] - value[6]) == (old_value[7] - value[7]) or
                    (value[6] - old_value[6]) == (old_value[7] - value[7])) and not (
                        old_value[6] == value[6] and old_value[7] == value[7]):
                    # Сбор значений с двух диагоналей
                    available_moovs[key] = value

                elif old_value[6] != value[6] and old_value[7] == value[7]:
                    available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    available_moovs[key] = value

            temp_available_moovs = dict(available_moovs)
            # Проверка на перекрытие движения
            for key, value in available_moovs.items():
                stop = Base_Mechanic.check_move(base, value, old_value, 0)
                if stop == 1:
                    del temp_available_moovs[key]

            available_moovs = temp_available_moovs


        # ********** КОРОЛЬ **************
        elif old_value[8] == 'Wight_King':

            for key, value in base.items():
                if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                        old_value[7] - value[7]):
                    if old_value[6] - value[6] == 1 or old_value[6] - value[6] == -1:
                        # Сбор значений с двух диагоналей
                        available_moovs[key] = value

                elif old_value[6] != value[6] and old_value[7] == value[7]:
                    if old_value[6] - value[6] == 1 or old_value[6] - value[6] == -1:
                        available_moovs[key] = value

                elif old_value[6] == value[6] and old_value[7] != value[7]:
                    if old_value[7] - value[7] == 1 or old_value[7] - value[7] == -1:
                        available_moovs[key] = value


        return available_moovs