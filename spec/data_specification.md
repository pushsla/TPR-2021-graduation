# Форматы данных
Все данные хранятся в формате JSON

## Шаблон меню
* id: int
* name: string название
* general: object основные параметры
    * eats_per_day: int число приемов пищи в день
    * no_eats_day: int число разгрузочных дней
    * all_products: list список всех наименований
    * vitamins: object содержание микроэлементов
        * "name": "value"
* menue: object меню
    * days: list of object дни Пн-Вс
        * [Object example] day
            * breakfast: object OR NONE прием пищи
                * [Object example] eat
                    * procucts: list список наименований
                    * dishes: list of object список блюд
                        * [Object example] dish
                            * products: list писок наименований
                            * recipe: str рецепт
            * breakfast2: object OR NONE прием пищи
            * dinner: object OR NONE прием пищи
            * dinner2: object OR NONE прием пищи
            * supper: object OR NONE прием пищи
            * supper2: object OR NONE прием пищи