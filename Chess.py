import copy
from tkinter import *
from PIL import Image, ImageTk


from shah import check_shah

# ***************ОСНОВА*******************
root = Tk()


# Название, возможность менять масштаб окна
root.title('Шахматы Православные')
root.resizable(height=False, width=False)


# icon
root.iconphoto(True, PhotoImage(file='pic/icon.png'))


canvas = Canvas(root, width=540, height=500)
canvas.pack()


class init:

    base = {
        'a1': [35.1, 425, 79.1, 475, 23.1, 419, 1, 1, 'None'],
        'a2': [35.1, 368.5, 79.1, 418.5, 23.1, 362.5, 2, 1, 'None'],
        'a3': [35.1, 312, 79.1, 362, 23.1, 306, 3, 1, 'None'],
        'a4': [35.1, 255.5, 79.1, 305.5, 23.1, 249.5, 4, 1, 'None'],
        'a5': [35.1, 199, 79.1, 249, 23.1, 193, 5, 1, 'None'],
        'a6': [35.1, 142.5, 79.1, 192.5, 23.1, 136.5, 6, 1, 'None'],
        'a7': [35.1, 86, 79.1, 136, 23.1, 80, 7, 1, 'None'],
        'a8': [35.1, 29.5, 79.1, 79.5, 23.1, 23.5, 8, 1, 'None'],

        'b1': [91.8, 425, 135.8, 475, 79.8, 419, 1, 2, 'None'],
        'b2': [91.8, 368.5, 135.8, 418.5, 79.8, 362.5, 2, 2, 'None'],
        'b3': [91.8, 312, 135.8, 362, 79.8, 306, 3, 2, 'None'],
        'b4': [91.8, 255.5, 135.8, 305.5, 79.8, 249.5, 4, 2, 'None'],
        'b5': [91.8, 199, 135.8, 249, 79.8, 193, 5, 2, 'None'],
        'b6': [91.8, 142.5, 135.8, 192.5, 79.8, 136.5, 6, 2, 'None'],
        'b7': [91.8, 86, 135.8, 136, 79.8, 80, 7, 2, 'None'],
        'b8': [91.8, 29.5, 135.8, 79.5, 79.8, 23.5, 8, 2, 'None'],

        'c1': [148.5, 425, 192.5, 475, 136.5, 419, 1, 3, 'None'],
        'c2': [148.5, 368.5, 192.5, 418.5, 136.5, 362.5, 2, 3, 'None'],
        'c3': [148.5, 312, 192.5, 362, 136.5, 306, 3, 3, 'None'],
        'c4': [148.5, 255.5, 192.5, 305.5, 136.5, 249.5, 4, 3, 'None'],
        'c5': [148.5, 199, 192.5, 249, 136.5, 193, 5, 3, 'None'],
        'c6': [148.5, 142.5, 192.5, 192.5, 136.5, 136.5, 6, 3, 'None'],
        'c7': [148.5, 86, 192.5, 136, 136.5, 80, 7, 3, 'None'],
        'c8': [148.5, 29.5, 192.5, 79.5, 136.5, 23.5, 8, 3, 'None'],

        'd1': [205.2, 425, 249.2, 475, 193.2, 419, 1, 4, 'None'],
        'd2': [205.2, 368.5, 249.2, 418.5, 193.2, 362.5, 2, 4, 'None'],
        'd3': [205.2, 312, 249.2, 362, 193.2, 306, 3, 4, 'None'],
        'd4': [205.2, 255.5, 249.2, 305.5, 193.2, 249.5, 4, 4, 'None'],
        'd5': [205.2, 199, 249.2, 249, 193.2, 193, 5, 4, 'None'],
        'd6': [205.2, 142.5, 249.2, 192.5, 193.2, 136.5, 6, 4, 'None'],
        'd7': [205.2, 86, 249.2, 136, 193.2, 80, 7, 4, 'None'],
        'd8': [205.2, 29.5, 249.2, 79.5, 193.2, 23.5, 8, 4, 'None'],

        'e1': [261.9, 425, 305.9, 475, 249.9, 419, 1, 5, 'None'],
        'e2': [261.9, 368.5, 305.9, 418.5, 249.9, 362.5, 2, 5, 'None'],
        'e3': [261.9, 312, 305.9, 362, 249.9, 306, 3, 5, 'None'],
        'e4': [261.9, 255.5, 305.9, 305.5, 249.9, 249.5, 4, 5, 'None'],
        'e5': [261.9, 199, 305.9, 249, 249.9, 193, 5, 5, 'None'],
        'e6': [261.9, 142.5, 305.9, 192.5, 249.9, 136.5, 6, 5, 'None'],
        'e7': [261.9, 86, 305.9, 136, 249.9, 80, 7, 5, 'None'],
        'e8': [261.9, 29.5, 305.9, 79.5, 249.9, 23.5, 8, 5, 'None'],

        'f1': [318.6, 425, 363.6, 475, 306, 419, 1, 6, 'None'],
        'f2': [318.6, 368.5, 363.6, 418.5, 306, 362.5, 2, 6, 'None'],
        'f3': [318.6, 312, 363.6, 362, 306, 306, 3, 6, 'None'],
        'f4': [318.6, 255.5, 363.6, 305.5, 306, 249.5, 4, 6, 'None'],
        'f5': [318.6, 199, 363.6, 249, 306, 193, 5, 6, 'None'],
        'f6': [318.6, 142.5, 363.6, 192.5, 306, 136.5, 6, 6, 'None'],
        'f7': [318.6, 86, 363.6, 136, 306, 80, 7, 6, 'None'],
        'f8': [318.6, 29.5, 363.6, 79.5, 306, 23.5, 8, 6, 'None'],

        'g1': [375.3, 425, 420.3, 475, 364.3, 419, 1, 7, 'None'],
        'g2': [375.3, 368.5, 420.3, 418.5, 364.3, 362.5, 2, 7, 'None'],
        'g3': [375.3, 312, 420.3, 362, 364.3, 306, 3, 7, 'None'],
        'g4': [375.3, 255.5, 420.3, 305.5, 364.3, 249.5, 4, 7, 'None'],
        'g5': [375.3, 199, 420.3, 249, 364.3, 193, 5, 7, 'None'],
        'g6': [375.3, 142.5, 420.3, 192.5, 364.3, 136.5, 6, 7, 'None'],
        'g7': [375.3, 86, 420.3, 136, 364.3, 80, 7, 7, 'None'],
        'g8': [375.3, 29.5, 420.3, 79.5, 364.3, 23.5, 8, 7, 'None'],

        'h1': [432, 425, 476, 475, 420, 419, 1, 8, 'None'],
        'h2': [432, 368.5, 476, 418.5, 420, 362.5, 2, 8, 'None'],
        'h3': [432, 312, 476, 362, 420, 306, 3, 8, 'None'],
        'h4': [432, 255.5, 476, 305.5, 420, 249.5, 4, 8, 'None'],
        'h5': [432, 199, 476, 249, 420, 193, 5, 8, 'None'],
        'h6': [432, 142.5, 476, 192.5, 420, 136.5, 6, 8, 'None'],
        'h7': [432, 86, 476, 136, 420, 80, 7, 8, 'None'],
        'h8': [432, 29.5, 476, 79.5, 420, 23.5, 8, 8, 'None'],

        # [0][1] - [x][y] лучшие точки для размещения картинок размером 45 на 45
        # [2][3] [4][5] - точки для начертания квадрата от левого верхнего угла до правого нижнего
        # [6][7] - матрица [y] [x]
        # [8] - тег с фигурой
    }

    # Рисуем поле
    for key, value in base.items():
        if value[6] == value[7] \
                or value[6] + 2 == value[7] \
                or value[6] + 4 == value[7] \
                or value[6] + 6 == value[7] \
                or value[6] - 2 == value[7] \
                or value[6] - 4 == value[7] \
                or value[6] - 6 == value[7]:

            canvas.create_rectangle(value[2], value[3], value[4], value[5], fill="#d3733a")
        else:
            canvas.create_rectangle(value[2], value[3], value[4], value[5], fill="#f5dfc3")


    white_types = [
        'Wight_Pawn',
        'Wight_Rook',
        'Wight_Knight',
        'Wight_Officer',
        'Wight_Queen',
        'Wight_King'
    ]

    black_types = [
        'Black_Pawn',
        'Black_Rook',
        'Black_Knight',
        'Black_Officer',
        'Black_Queen',
        'Black_King'
    ]

    # Очередь хода
    # [1] Белые [2] Черные
    turn = [1, 0]

    # Список ходов
    moove_keys = []

    # id фигур, используется для удаления
    chess_list = []

class BaseMechanic:

    def flag(self, value, overlapping_objects):
        # Для предотвращения спама дубликатов в chess_list
        flag = False
        for obj_id in overlapping_objects:
            if obj_id in init.chess_list:
                flag = True
                break
        if not flag:  # эквивалентно: if flag = False:
            init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Rook, anchor=NW))

    def update(self, base, old_value, new_value):
        for key, value in base.items():
            if value[8] == 'Wight_Rook':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:  # эквивалентно: if flag = False:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Rook, anchor=NW))

            elif value[8] == 'Wight_Knight':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Knight, anchor=NW))

            elif value[8] == 'Wight_King':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_King, anchor=NW))

            elif value[8] == 'Wight_Pawn':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Pawn, anchor=NW))


            elif value[8] == 'Wight_Officer':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Officer, anchor=NW))

            elif value[8] == 'Wight_Queen':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Wight_Queen, anchor=NW))

            elif value[8] == 'Black_Pawn':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_Pawn, anchor=NW))

            elif value[8] == 'Black_Knight':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_Knight, anchor=NW))

            elif value[8] == 'Black_Officer':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_Officer, anchor=NW))

            elif value[8] == 'Black_Rook':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_Rook, anchor=NW))

            elif value[8] == 'Black_Queen':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_Queen, anchor=NW))

            elif value[8] == 'Black_King':
                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])

                # Для предотвращения спама дубликатов в chess_list
                flag = False
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        flag = True
                        break
                if not flag:
                    init.chess_list.append(canvas.create_image(value[0], value[1], image=Black_King, anchor=NW))


            elif old_value[8] == 'None':
                # Удаление фигуры со старой клетки
                overlapping_objects = canvas.find_overlapping(old_value[2], old_value[3], old_value[4], old_value[5])
                # print(overlapping_objects, (' То что видит find_overlapping'))
                for obj_id in overlapping_objects:
                    if obj_id in init.chess_list:
                        canvas.delete(obj_id)
                        init.chess_list.remove(obj_id)
                    else:
                        continue


    def check_move(self, base, new_value, old_value, stop):

        # Проверка на перекрытие движения
            # Вертикальное движение
            if new_value[6] != old_value[6] and new_value[7] == old_value[7]:
                for key, value in base.items():
                    if old_value[6] + 1 <= value[6] <= new_value[6] - 1 or old_value[6] - 1 >= value[6] >= new_value[6] + 1:
                        # print(f"Тег для {key} в вертикали: {value[8]}")
                        if value[8] != 'None' and value[7] == old_value[7]:
                            stop = 1
                        else:
                            continue

            # Горизонтальное движение
            if new_value[7] != old_value[7] and new_value[6] == old_value[6]:
                for key, value in base.items():
                    if old_value[7] + 1 <= value[7] <= new_value[7] - 1 or old_value[7] - 1 >= value[7] >= new_value[7] + 1:
                        # print(f"Тег для {key} в горизонтали: {value[8]}")
                        if value[8] != 'None' and value[6] == old_value[6]:
                            stop = 1
                        else:
                            continue


            # Диагональное движение
            if new_value[7] != old_value[7] and new_value[6] != old_value[6]:
                spisok = {}
                end = 0

                while end == 0:
                    for key, value in base.items():
                        if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                                old_value[7] - value[7]):
                            # Сбор значений с двух диагоналей
                            spisok[key] = value

                            # print(spisok)
                            end = 1

                for key, value in spisok.items():
                    # Правый вверх
                    if old_value[6] + 1 <= value[6] <= new_value[6] - 1 and old_value[7] + 1 <= value[7] <= new_value[7] - 1:
                        # print(f"Тег для {key} в диагонали: {value[8]}")
                        if value[8] != 'None':
                            stop = 1
                            break
                            # spisok.clear()
                        else:
                            continue

                    # Левый вверх
                    elif old_value[6] + 1 <= value[6] <= new_value[6] - 1 and old_value[7] - 1 >= value[7] >= new_value[
                        7] + 1:
                        # print(f"Тег для {key} в диагонали: {value[8]}")
                        if value[8] != 'None':
                            stop = 1
                            break
                        else:
                            continue

                    # Правый низ
                    elif old_value[6] - 1 >= value[6] >= new_value[6] + 1 and old_value[7] + 1 <= value[7] <= new_value[7] - 1:
                        # print(f"Тег для {key} в диагонали: {value[8]}")
                        if value[8] != 'None':
                            stop = 1
                            break
                        else:
                            continue

                    # Левый низ
                    elif old_value[6] - 1 >= value[6] >= new_value[6] + 1 and old_value[7] - 1 >= value[7] >= new_value[7] + 1:
                        # print(f"Тег для {key} в диагонали: {value[8]}")
                        if value[8] != 'None':
                            stop = 1
                            break
                        else:
                            continue

                spisok.clear()

            return stop


    def find_closest_point(self, base, x, y):

        closest_point = None

        for key, value in base.items():
            distance = [x, y]
            if distance[0] < value[2] and distance[1] < value[3] and distance[0] > value[4] and distance[1] > value[5]:
                closest_point = key, value
                # print('closest_point равен', closest_point)
                break
            else:
                continue

        # Проверка на клик вне поля
        if closest_point is not None:
            return closest_point


    def check_destroy_mooves(self, new_key, base, new_value, old_value, old_key, figure):

        # Условная переменная,
        # первое значение при изменении останавливает код,
        # второе создает белого ферзя, третье черного (для пешек на 8-1 полях)
        prom_result = [0, 0, 0]

        # [6] = y
        # [7] = x
        if old_value[8] in init.black_types:
            # Если ход черных
            if init.turn[1] == 1:

                # Формула Шаха
                # Проверка на шах белым в результате действия белых
                copy_base = copy.deepcopy(init.base)
                copy_base[old_key][8] = 'None'
                copy_base[new_key][8] = str(figure)

                white_moovs = {}

                for key, value in copy_base.items():

                    # Проверка всех возможных ходов белых
                    if value[8] in init.white_types:
                        nold_value = value
                        available_oovs = check_shah(new_key, copy_base, new_value, old_key, nold_value, init, Base_Mechanic)
                        # print(available_oovs, f'ПРОВЕРКА ШАХА ДЛЯ {key} {nold_value[8]}')
                        white_moovs.update(available_oovs)

                    for key, value in white_moovs.items():
                        if value[8] == 'Black_King':
                            white_moovs.clear()
                            copy_base.clear()

                            prom_result[0] = 1
                            return prom_result

                white_moovs.clear()
                copy_base.clear()

                # ********** ПЕШКА **************
                if old_value[8] == 'Black_Pawn':

                    available_moovs = {}

                    # Создание списка доступных ходов
                    for key, value in base.items():
                        if value[6] == old_value[6] - 1 and value[7] == old_value[7] and value[8] == 'None':
                            available_moovs[key] = value
                        elif new_value[6] == old_value[6] - 2 and old_value[6] == 7 and new_value[7] == old_value[7] and \
                                new_value[8] == 'None':
                            available_moovs[key] = value

                        # Взятие фигур
                        elif new_value[6] == old_value[6] - 1 and new_value[7] == old_value[7] + 1 and new_value[
                            8] in init.white_types \
                                or new_value[6] == old_value[6] - 1 and new_value[7] == old_value[7] - 1 and new_value[
                            8] in init.white_types:
                            available_moovs[key] = value

                        # Проверка на двойной ход вражеской пешки возле нашей
                        # С правой стороны
                        elif value[6] == old_value[6] and value[7] == old_value[7]+1 and value[8] == 'Wight_Pawn' and new_value[6] == old_value[6] - 1 and new_value[7] == old_value[7] + 1:
                            print('Взятие на проходе', key, value[8])
                            qw1, qw2 = init.moove_keys[-1]
                            q, w = qw1
                            w = int(w)

                            e, r = qw2
                            r = int(r)
                            # Проверка на двойной ход вражеской пешки
                            if key == qw2 and r - w == 2:
                                value[8] = 'None'

                                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                                for obj_id in overlapping_objects:
                                    if obj_id in init.chess_list:
                                        canvas.delete(obj_id)
                                        init.chess_list.remove(obj_id)
                                available_moovs[new_key] = new_value
                            else:
                                pass

                        # С левой стороны
                        elif value[6] == old_value[6] and value[7] == old_value[7] - 1 and value[8] == 'Wight_Pawn' and new_value[6] == old_value[6] - 1 and new_value[7] == old_value[7] - 1:
                            print('Взятие на проходе', key, value[8])
                            qw1, qw2 = init.moove_keys[-1]
                            q, w = qw1
                            w = int(w)

                            e, r = qw2
                            r = int(r)
                            # Проверка на двойной ход вражеской пешки
                            if key == qw2 and r - w == 2:
                                value[8] = 'None'

                                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                                for obj_id in overlapping_objects:
                                    if obj_id in init.chess_list:
                                        canvas.delete(obj_id)
                                        init.chess_list.remove(obj_id)
                                available_moovs[new_key] = new_value
                            else:
                                pass

                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    # Проверка на ход в свою фигуру
                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    # Создание ферзя
                    if new_value[6] == 1 and new_value in available_moovs.values():
                        overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                      new_value[5])
                        for obj_id in overlapping_objects:
                            if obj_id in init.chess_list:
                                canvas.delete(obj_id)
                                init.chess_list.remove(obj_id)

                        prom_result[2] = 1  # Создаем ферзя

                        base[new_key][8] = 'Black_Queen'
                        Base_Mechanic.update(base, old_value, new_value)


                    if new_value[8] in init.white_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** КОНЬ **************
                elif old_value[8] == 'Black_Knight':
                    available_moovs = {}
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

                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    # Проверка на ход в свою фигуру
                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    # Взятие чужой
                    if new_value[8] in init.white_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result
                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** СЛОН **************
                elif old_value[8] == 'Black_Officer':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                                old_value[7] - value[7]):
                            # Сбор значений с двух диагоналей
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.white_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** ЛАДЬЯ **************
                elif old_value[8] == 'Black_Rook':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if old_value[6] != value[6] and old_value[7] == value[7]:
                            available_moovs[key] = value

                        elif old_value[6] == value[6] and old_value[7] != value[7]:
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.white_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** ФЕРЗЬ **************
                elif old_value[8] == 'Black_Queen':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                                old_value[7] - value[7]):
                            # Сбор значений с двух диагоналей
                            available_moovs[key] = value

                        elif old_value[6] != value[6] and old_value[7] == value[7]:
                            available_moovs[key] = value

                        elif old_value[6] == value[6] and old_value[7] != value[7]:
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    # Ликвидация
                    if new_value[8] in init.white_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** КОРОЛЬ **************
                elif old_value[8] == 'Black_King':

                    # Создаем список доступных ходов

                    available_moovs = {}
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

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.white_types and new_value in available_moovs.values():

                        overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                      new_value[5])
                        for obj_id in overlapping_objects:
                            if obj_id in init.chess_list:
                                canvas.delete(obj_id)
                                init.chess_list.remove(obj_id)
                            else:
                                continue

                        # Проверка на ход в свою фигуру

                        Init.base[new_key][8] = old_value[8]
                        Base_Mechanic.update(base, old_value, new_value)
                        prom_result[0] = 0

                    return prom_result
            else:
                prom_result[0]=1
                return prom_result

        if old_value[8] in init.white_types:

            # Если ход белых
            if init.turn[0] == 1:

                # Формула Шаха
                # Проверка на шах белым в результате действия белых
                copy_base = copy.deepcopy(init.base)
                copy_base[old_key][8] = 'None'
                copy_base[new_key][8] = str(figure)

                black_moovs = {}

                for key, value in copy_base.items():

                    # Проверка всех возможных ходов черных
                    if value[8] in init.black_types:
                        nold_value = value
                        available_oovs = check_shah(new_key, copy_base, new_value, old_key, nold_value, init, Base_Mechanic)
                        # print(available_oovs, f'ПРОВЕРКА ШАХА ДЛЯ {key} {nold_value[8]}')
                        black_moovs.update(available_oovs)

                    for key, value in black_moovs.items():
                        if value[8] == 'Wight_King':
                            black_moovs.clear()
                            copy_base.clear()

                            prom_result[0] = 1
                            return prom_result

                black_moovs.clear()
                copy_base.clear()


                # ********** ПЕШКА **************
                if old_value[8] == 'Wight_Pawn':
                    available_moovs = {}
                    for key, value in base.items():
                        if value[6] == old_value[6] + 1 and value[7] == old_value[7] and value[8] == 'None':
                            available_moovs[key] = value
                        elif new_value[6] == old_value[6]+2 and old_value[6] == 2 and new_value[7] == old_value[7] and new_value[8] == 'None':
                            available_moovs[key] = value

                        elif new_value[6] == old_value[6] + 1 and new_value[7] == old_value[7] + 1 and new_value[8] in init.black_types \
                                or new_value[6] == old_value[6] + 1 and new_value[7] == old_value[7] - 1 and new_value[8] in init.black_types:
                            available_moovs[key] = value

                        # Проверка на двойной ход вражеской пешки возле нашей
                        # С правой стороны
                        elif value[6] == old_value[6] and value[7] == old_value[7]+1 and value[8] == 'Black_Pawn' and new_value[6] == old_value[6] + 1 and new_value[7] == old_value[7] + 1:
                            print('Взятие на проходе', key, value[8])
                            qw1, qw2 = init.moove_keys[-1]
                            q, w = qw1
                            w = int(w)

                            e, r = qw2
                            r = int(r)
                            # Проверка на двойной ход вражеской пешки
                            if key == qw2 and r - w == -2:
                                value[8] = 'None'

                                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                                for obj_id in overlapping_objects:
                                    if obj_id in init.chess_list:
                                        canvas.delete(obj_id)
                                        init.chess_list.remove(obj_id)
                                available_moovs[new_key] = new_value
                            else:
                                pass

                        # С левой стороны
                        elif value[6] == old_value[6] and value[7] == old_value[7]-1 and value[8] == 'Black_Pawn' and new_value[6] == old_value[6] + 1 and new_value[7] == old_value[7] - 1:
                            print('Взятие на проходе', key, value[8])
                            qw1, qw2 = init.moove_keys[-1]
                            q, w = qw1
                            w = int(w)

                            e, r = qw2
                            r = int(r)
                            # Проверка на двойной ход вражеской пешки
                            if key == qw2 and r - w == -2:
                                value[8] = 'None'

                                overlapping_objects = canvas.find_overlapping(value[2], value[3], value[4], value[5])
                                for obj_id in overlapping_objects:
                                    if obj_id in init.chess_list:
                                        canvas.delete(obj_id)
                                        init.chess_list.remove(obj_id)
                                available_moovs[new_key] = new_value
                            else:
                                pass

                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[6] == 8 and new_value in available_moovs.values():
                        overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4], new_value[5])
                        for obj_id in overlapping_objects:
                            if obj_id in init.chess_list:
                                canvas.delete(obj_id)
                                init.chess_list.remove(obj_id)

                        prom_result[1] = 1  # Создаем ферзя

                        base[new_key][8] = 'Wight_Queen'
                        Base_Mechanic.update(base, old_value, new_value)

                    if new_value[8] in init.black_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0


                    return prom_result


                # ********** КОНЬ **************
                elif old_value[8] == 'Wight_Knight':
                    available_moovs = {}
                    for key, value in base.items():
                        #Легендарная формула просчета движения коня
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

                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    # Проверка на ход в свою фигуру
                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    # Взятие чужой
                    if new_value[8] in init.black_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0


                    return prom_result

                # ********** СЛОН **************
                elif old_value[8] == 'Wight_Officer':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                                        old_value[7] - value[7]):
                            # Сбор значений с двух диагоналей
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.black_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0


                    return prom_result

                # ********** ЛАДЬЯ **************
                elif old_value[8] == 'Wight_Rook':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if old_value[6] != value[6] and old_value[7] == value[7]:
                            available_moovs[key] = value

                        elif old_value[6] == value[6] and old_value[7] != value[7]:
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.black_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0


                    return prom_result

                # ********** ФЕРЗЬ **************
                elif old_value[8] == 'Wight_Queen':

                    # Создаем список доступных ходов для ферзя
                    available_moovs = {}
                    for key, value in base.items():
                        if (old_value[6] - value[6]) == (old_value[7] - value[7]) or (value[6] - old_value[6]) == (
                                        old_value[7] - value[7]):
                            # Сбор значений с двух диагоналей
                            available_moovs[key] = value

                        elif old_value[6] != value[6] and old_value[7] == value[7]:
                            available_moovs[key] = value

                        elif old_value[6] == value[6] and old_value[7] != value[7]:
                            available_moovs[key] = value

                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1

                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    # Ликвидация
                    if new_value[8] in init.black_types and new_value in available_moovs.values():
                        stop = Base_Mechanic.check_move(base, new_value, old_value, 0)
                        if stop == 1:
                            prom_result[0] = 1
                            return prom_result

                        else:
                            overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                          new_value[5])
                            for obj_id in overlapping_objects:
                                if obj_id in init.chess_list:
                                    canvas.delete(obj_id)
                                    init.chess_list.remove(obj_id)
                                else:
                                    continue
                            Init.base[new_key][8] = old_value[8]
                            Base_Mechanic.update(base, old_value, new_value)
                            prom_result[0] = 0

                    return prom_result

                # ********** КОРОЛЬ **************
                elif old_value[8] == 'Wight_King':

                    # Создаем список доступных ходов

                    available_moovs = {}
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



                    # Эквивалентно стандартному иф элсе
                    prom_result[0] = 0 if new_value in available_moovs.values() else 1


                    if old_value[8] in init.white_types and new_value[8] in init.white_types or \
                            old_value[8] in init.black_types and new_value[8] in init.black_types:
                        prom_result[0] = 1
                        return prom_result
                    else:
                        pass

                    if new_value[8] in init.black_types and new_value in available_moovs.values():

                        overlapping_objects = canvas.find_overlapping(new_value[2], new_value[3], new_value[4],
                                                                      new_value[5])
                        for obj_id in overlapping_objects:
                            if obj_id in init.chess_list:
                                canvas.delete(obj_id)
                                init.chess_list.remove(obj_id)
                            else:
                                continue

                        # Проверка на ход в свою фигуру


                        Init.base[new_key][8] = old_value[8]
                        Base_Mechanic.update(base, old_value, new_value)
                        prom_result[0] = 0

                    # Очистка списка чтобы не забивать память
                    available_moovs.clear()
                    return prom_result

            else:
                prom_result[0]=1
                return prom_result

def castling(new_key, base, new_value, old_value, old_key, figure):
    # Рокировка.
    # [0] право низ, [1] лево низ, [2] право вверх, [3], лево вверх
    cruel = [0, 0, 0, 0]
    # Ход белых
    if init.turn[0] == 1:
        for key, value in init.base.items():
            if new_key == 'g1' and old_value[8] == 'Wight_King':
                if any('h1' in sublist for sublist in init.moove_keys) or any('e1' in sublist for sublist in init.moove_keys):
                    pass
                else:
                    if key == 'f1' and value[8] == 'None':
                        cruel[0] += 0.5
                    elif key == 'g1' and value[8] == 'None':
                        cruel[0] += 0.5

            elif new_key == 'c1' and old_value[8] == 'Wight_King':
                if any('a1' in sublist for sublist in init.moove_keys) or any('e1' in sublist for sublist in init.moove_keys):
                    pass
                else:
                    if key == 'd1' and value[8] == 'None':
                        cruel[1] += 0.3
                    elif key == 'c1' and value[8] == 'None':
                        cruel[1] += 0.3
                    elif key == 'b1' and value[8] == 'None':
                        cruel[1] += 0.4
                    else:
                        pass
        # Формула Шаха
        # Проверка на шах белым в результате действия белых
        copy_base = copy.deepcopy(init.base)

        black_moovs = {}

        for key, value in copy_base.items():

            # Проверка всех возможных ходов белых
            if value[8] in init.black_types:
                nold_value = value
                available_oovs = check_shah(new_key, copy_base, new_value, old_key, nold_value, init, Base_Mechanic)
                black_moovs.update(available_oovs)

        for key, value in black_moovs.items():
            if key == 'g1' or key == 'f1':
                cruel[0] = 0
            elif key == 'd1' or key == 'c1':
                cruel[1] = 0
            else:
                pass

        black_moovs.clear()
        copy_base.clear()


    # Ход черных
    elif init.turn[1] == 1:
        for key, value in init.base.items():
            if new_key == 'g8' and old_value[8] == 'Black_King':
                if any('h8' in sublist for sublist in init.moove_keys) or any('e8' in sublist for sublist in init.moove_keys):
                    pass
                else:
                    if key == 'f8' and value[8] == 'None':
                        cruel[2] += 0.5
                    elif key == 'g8' and value[8] == 'None':
                        cruel[2] += 0.5
                    else:
                        pass

            elif new_key == 'c8' and old_value[8] == 'Black_King':
                if any('a8' in sublist for sublist in init.moove_keys) or any('e8' in sublist for sublist in init.moove_keys):
                    pass
                else:
                    if key == 'd8' and value[8] == 'None':
                        cruel[3] += 0.3
                    elif key == 'c8' and value[8] == 'None':
                        cruel[3] += 0.3
                    elif key == 'b8' and value[8] == 'None':
                        cruel[3] += 0.4
                    else:
                        pass
    else:
        pass

    # Формула Шаха
    # Проверка на шах белым в результате действия белых
    copy_base = copy.deepcopy(init.base)

    white_moovs = {}

    for key, value in copy_base.items():

        # Проверка всех возможных ходов белых
        if value[8] in init.white_types:
            nold_value = value
            available_oovs = check_shah(new_key, copy_base, new_value, old_key, nold_value, init, Base_Mechanic)
            white_moovs.update(available_oovs)

    for key, value in white_moovs.items():
        if key == 'g8' or key == 'f8':
            cruel[2] = 0
        elif key == 'd8' or key == 'c8':
            cruel[3] = 0
        else:
            pass


    white_moovs.clear()
    copy_base.clear()

    return cruel





def first_click(event, base):
    x = event.x
    y = event.y
    print(f"Первый Клик по координатам x={x}, y={y}")


    closest_point = Base_Mechanic.find_closest_point(base, x, y)
    if closest_point is not None:
        old_key, old_value = closest_point
        print(old_key, old_value)
    else:
        canvas.bind('<Button-1>', lambda event: first_click(event, base))
        print("Ближайшая точка не найдена")
        return

    figure = old_value[8]


    # Проверка на пустое поле
    if figure != 'None':
        canvas.bind('<Button-1>', lambda event: second_click(event, old_key, old_value, figure, base))
    else:
        print('Выберите фигуру')
        canvas.bind('<Button-1>', lambda event: first_click(event, base))


def second_click(event, old_key, old_value, figure, base):

    # old_key - Индекс клетки первого клика
    # old_value - Свойства клетки первого клика
    # figure - (old_value[8]) Восьмое поле, фигура
    # base - общий словарь с клетками

    # new_key - Индекс клетки второго клика
    # new_value - Свойства клетки второго клика

    # stop - условная переменная для возврата кода к first_click

    x = event.x
    y = event.y

    stop = 0
    cruel = [0, 0, 0, 0]

    closest_point = Base_Mechanic.find_closest_point(base, x, y)
    if closest_point is not None:
        new_key, new_value = closest_point
    else:
        canvas.bind('<Button-1>', lambda event: first_click(event, base))
        print("Ближайшая точка не найдена")
        return


    stop = Base_Mechanic.check_move(base, new_value, old_value, stop)




    # Проверка на двойной клик по одному и тому же полю
    if old_key == new_key:
        stop = 1


    # Проверка на фигуру
    if old_value[8] != 'None':
        prom_result = Base_Mechanic.check_destroy_mooves(new_key, base, new_value, old_value, old_key, figure)
        print(prom_result, 'ПРОМТРЕЗУЛТ')
        if prom_result != None:
            if prom_result[0] == 1:
                cruel = castling(new_key, base, new_value, old_value, old_key, figure)
                print(cruel, 'CRUEL')
                if cruel[0] == 1 or cruel[1] == 1 or cruel[2] == 1 or cruel[3] == 1:
                    pass
                else:
                    stop = 1
            elif prom_result[1] == 1:
                figure = 'Wight_Queen'
            elif prom_result[2] == 1:
                figure = 'Black_Queen'
            elif prom_result == None:
                pass
            else:
                pass


    if stop == 1:
        canvas.bind('<Button-1>', lambda event: first_click(event, base))
        return
    print('stop равен', stop)



    # Проверка на рокировку
    if cruel[0] == 1:
        print(f"Второй Клик по координатам x={x}, y={y}")
        base[old_key][8] = 'None'
        base['h1'][8] = 'None'

        base['f1'][8] = 'Wight_Rook'
        base[str(new_key)][8] = str(figure)

        overlapping_objects = canvas.find_overlapping(476, 475, 420, 419)
        for obj_id in overlapping_objects:
            if obj_id in init.chess_list:
                canvas.delete(obj_id)
                init.chess_list.remove(obj_id)

        Base_Mechanic.update(base, old_value, new_value)
        print(init.chess_list, 'chess_list')

    elif cruel[1] == 1:
        print(f"Второй Клик по координатам x={x}, y={y}")
        base[old_key][8] = 'None'
        base['a1'][8] = 'None'

        base['d1'][8] = 'Wight_Rook'
        base[str(new_key)][8] = str(figure)

        overlapping_objects = canvas.find_overlapping(79.1, 475, 23.1, 419)
        for obj_id in overlapping_objects:
            if obj_id in init.chess_list:
                canvas.delete(obj_id)
                init.chess_list.remove(obj_id)

        Base_Mechanic.update(base, old_value, new_value)
        print(init.chess_list, 'chess_list')

    elif cruel[2] == 1:
        print(f"Второй Клик по координатам x={x}, y={y}")
        base[old_key][8] = 'None'
        base['h8'][8] = 'None'

        base['f8'][8] = 'Black_Rook'
        base[str(new_key)][8] = str(figure)

        overlapping_objects = canvas.find_overlapping(476, 79.5, 420, 23.5)
        for obj_id in overlapping_objects:
            if obj_id in init.chess_list:
                canvas.delete(obj_id)
                init.chess_list.remove(obj_id)

        Base_Mechanic.update(base, old_value, new_value)
        print(init.chess_list, 'chess_list')


    elif cruel[3] == 1:
        print(f"Второй Клик по координатам x={x}, y={y}")
        base[old_key][8] = 'None'
        base['a8'][8] = 'None'

        base['d8'][8] = 'Black_Rook'
        base[str(new_key)][8] = str(figure)

        overlapping_objects = canvas.find_overlapping(79.1, 79.5, 23.1, 23.5)
        for obj_id in overlapping_objects:
            if obj_id in init.chess_list:
                canvas.delete(obj_id)
                init.chess_list.remove(obj_id)

        Base_Mechanic.update(base, old_value, new_value)
        print(init.chess_list, 'chess_list')

    elif cruel[0] < 1 and cruel[0] > 0 or cruel[1] < 1 and cruel[1] > 0 or cruel[2] < 1 and cruel[2] > 0 or cruel[3] < 1 and cruel[3] > 0:
        canvas.bind('<Button-1>', lambda event: first_click(event, base))
        return

    else:
        print(f"Второй Клик по координатам x={x}, y={y}")
        base[old_key][8] = 'None'
        base[str(new_key)][8] = str(figure)

        Base_Mechanic.update(base, old_value, new_value)
        print(init.chess_list, 'chess_list')

    # Список
    init.moove_keys.append([old_key, new_key])
    update_listbox(listbox)



    # init.turn[0] = 1 ход белых
    # init.turn[1] = 0 ход черных

    print(new_key, new_value)

    # Передача хода
    if init.turn[0] == 1 and init.turn[1] == 0:
        init.turn[0] = 0
        init.turn[1] = 1
    else:
        init.turn[0] = 1
        init.turn[1] = 0

    # print(base)
    canvas.bind('<Button-1>', lambda event: first_click(event, base))



# Добавляем фигуры на доску

# Wight

Wight_Pawn = Image.open('pic/Wight_Pawn.png')
Wight_Pawn = ImageTk.PhotoImage(Wight_Pawn)

Wight_Knight = Image.open('pic/Wight_Knight.png')
Wight_Knight = ImageTk.PhotoImage(Wight_Knight)

Wight_Officer = Image.open('pic/Wight_Officer.png')
Wight_Officer = ImageTk.PhotoImage(Wight_Officer)

Wight_Queen = Image.open('pic/Wight_Queen.png')
Wight_Queen = ImageTk.PhotoImage(Wight_Queen)

Wight_Rook = Image.open('pic/Wight_Rook.png')
Wight_Rook = ImageTk.PhotoImage(Wight_Rook)

Wight_King = Image.open('pic/Wight_King.png')
Wight_King = ImageTk.PhotoImage(Wight_King)

# Black

Black_Pawn = Image.open('pic/Black_Pawn.png')
Black_Pawn = ImageTk.PhotoImage(Black_Pawn)

Black_Knight = Image.open('pic/Black_Knight.png')
Black_Knight = ImageTk.PhotoImage(Black_Knight)

Black_Officer = Image.open('pic/Black_Officer.png')
Black_Officer = ImageTk.PhotoImage(Black_Officer)

Black_Queen = Image.open('pic/Black_Queen.png')
Black_Queen = ImageTk.PhotoImage(Black_Queen)

Black_Rook = Image.open('pic/Black_Rook.png')
Black_Rook = ImageTk.PhotoImage(Black_Rook)

Black_King = Image.open('pic/Black_King.png')
Black_King = ImageTk.PhotoImage(Black_King)



base = init.base


base['a1'][8] = 'Wight_Rook'
base['h1'][8] = 'Wight_Rook'

base['b1'][8] = 'Wight_Knight'
base['g1'][8] = 'Wight_Knight'

base['c1'][8] = 'Wight_Officer'
base['f1'][8] = 'Wight_Officer'

base['e1'][8] = 'Wight_King'
base['d1'][8] = 'Wight_Queen'

base['a2'][8] = 'Wight_Pawn'
base['b2'][8] = 'Wight_Pawn'
base['c2'][8] = 'Wight_Pawn'
base['d2'][8] = 'Wight_Pawn'
base['e2'][8] = 'Wight_Pawn'
base['f2'][8] = 'Wight_Pawn'
base['g2'][8] = 'Wight_Pawn'
base['h2'][8] = 'Wight_Pawn'




base['h8'][8] = 'Black_Rook'
base['a8'][8] = 'Black_Rook'

base['g8'][8] = 'Black_Knight'
base['b8'][8] = 'Black_Knight'

base['c8'][8] = 'Black_Officer'
base['f8'][8] = 'Black_Officer'

base['e8'][8] = 'Black_King'
base['d8'][8] = 'Black_Queen'

base['a7'][8] = 'Black_Pawn'
base['b7'][8] = 'Black_Pawn'
base['c7'][8] = 'Black_Pawn'
base['d7'][8] = 'Black_Pawn'
base['e7'][8] = 'Black_Pawn'
base['f7'][8] = 'Black_Pawn'
base['g7'][8] = 'Black_Pawn'
base['h7'][8] = 'Black_Pawn'


# ***************СПИСОК ХОДОВ*****************
def update_listbox(listbox):
    listbox.delete(0, END)  # Очистить содержимое Listbox
    # print('Список ходов:')
    for old_key in init.moove_keys:
        # print(old_key)
        listbox.insert(END, old_key)  # Добавить в Listbox


# Создаем список (Listbox)
listbox = Listbox(root, selectmode=SINGLE)
listbox.pack(padx=10, pady=10)

# Изменяем ширину и высоту списка
new_width = 7
new_height = 5
listbox.config(width=new_width, height=new_height)

# Размещаем список на холсте в координатах (x, y)
x, y = 485, 23
canvas.create_window(x, y, anchor=NW, window=listbox)

# ********************************************




Init = init()

Base_Mechanic = BaseMechanic()
Base_Mechanic.update(base, base['a1'], base['a1'])

print(init.chess_list, 'chess_list')




canvas.bind('<Button-1>', lambda event: first_click(event, base))

root.mainloop()

