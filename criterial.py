import json


class Criterial:
    """
    Модуль решения задачи многокритериальной оптимизации.
    Задача: Требуется из списка шаблонов меню выбрать, используя параметры клиента, несколько оптимальных вариантов шаблонов меню.

    Модуль содержит класс, реализующий следующие методы:
    Загрузка списка шаблонов меню в формате JSON (см data_specification.md) с диска
    Добавление нового шаблона
    Изменение существующего шаблона
    Сохранение шаблонов на диск
    Выбор N отпимальных вариантов по критериям клиента из зугруженного ранее списка

    Все методы следует сделать @classmethod, т.к используется паттерн "Singletone".

    В качестве параметров клиента предлагается использовать следующие величины:
    Возраст
    Тип физической активности
    Объём физической активности
    Цель использования диеты
    Аллергические реакции
    Любимые продукты

    Любая величина, для которой существует четко определенное количество вариантов (например цель использования диеты),
    должна быть реализована в виде соответствующей сущности Python так, чтобы невозможно было подставить значение,
    не определенное в коде, без ошибки.
    """

    def __init__(self):
        """Constructor"""
        self.menu_list = []
        self.filename = ''

    def load(self, filename):
        """ Загрузка списка шаблонов меню в формате JSON (см data_specification.md) с диска """
        self.filename = filename
        with open(filename, "r") as read_file:
            self.menu_list = json.load(read_file)

    def save(self, filename=None):
        """ Сохранение шаблонов на диск """
        filename = filename if filename else self.filename
        with open(filename, "w") as write_file:
             json.dump(self.menu_list, write_file)

    def change(self, id=0, newdata={}):
        """ Изменение существующего шаблона """
        for i, v in enumerate(self.menu_list):
            if v['id'] == id:
               self.menu_list[i] = newdata

    def append(self, newdata):
        """ Добавление нового шаблона """
        if not list(filter(lambda x: x['id'] == newdata['id'], self.menu_list)):
            self.menu_list.append(newdata)


if __name__ == "__main__":
    exmen = {
        "id": 1,
        "name": "for bodybuilders",
        "general": {
            "eats_per_day": 4,
            "type": "gain",
            "no_eats_day": 1,
            "all_products": ['milk', 'meat', 'banana', 'apple'],
            "vitamins": {
                "C": 20,
                "B6": 12,
                "E": 10
            }
        },
        "menue": {
            "Monday": {
                "breakfast": {
                    "eat": {
                        "products": ['pasta', 'chicken'],
                        "recipe": "ex"
                    }
                },
                "dinner": {
                    "eat": {
                        "products": ['carrot', 'onion'],
                        "recipe": "ex2"
                    }
                },
                "supper": {
                    "eat": {
                        "products": ['bread', 'butter'],
                        "recipe": "ex3"
                    }
                }
            }
        }
    }

    c1 = Criterial()
    c1.append(exmen)
    c1.append(exmen)
    c1.save()

    c2 = Criterial()
    c2.load()
    print(c2.menu_list)