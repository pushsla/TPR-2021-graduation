# Курсовая работа по ТПР 2021
Разработка системы поддержки принятия решений диетологом при составлении
рациона питания

## Motivation


## Realisation

Чтобы выбрать из всего многообразия шаблонов рационов питания применяется **алгоритм анализа иерархий**.

Для "подстройки" выбранного шаблона под нужды конкретного человека используется **лрегрессионная модель**.

### Алгоритм анализа иерархий
Реализован в виде класса Python с использованием паттерна "Singletone".
Суть алгоритма в следующем:

*На основании передаваемых параметров, характеризующих предпочтения
и физеологические данные клиента выбрать два самых подходящих шаблона
рациона питания для дальнейшей обработки специалистом-диетологом*

Каждый из представленных шаблонов программ питания имеет отвечающий параметрам
характеристики, благодаря чему имеет место решение задачи многокритериальной
оптимизации.

Подробная спецификация для разработчика находится в файле **spec/criterial.md**

### Регрессионная модель
Представляет собой коллекцию заранее обученных на параметрах множества людей моделей,
решающих задачу аппроксимации зависимостей характеристик пользователей и рационов питания.

При подборе чоответствующей характеристики используется
отвечающая этой характеристике регрессионная модель.

## Credits