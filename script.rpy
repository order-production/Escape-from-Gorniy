# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define k = Character(u'Кетон', color="#c8ffc8")
define b = Character(u'Василий', color="#ff6666")

define ppoints = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# Разрешение фона 1280 на 720, персонаженй 640 на 360

# Игра начинается здесь:
init:
    image bg uni = "gora 5.jpg"
    image bg uni1 = "5.jpg"
    image mks = "mks.png"
    image mks smile = "mks smile.png"
    image bg = "bg.png"
label start:
    scene bg uni with dissolve
    "\"MKS\" представляет... \nEscape from Gorniy"
    scene bg uni1 with fade
    "Тест"
    "{i}Эта надпись будет курсивом.{/i}"
    "{u}Надпись {b}жирная{/b}{/u}"
    "???" "Привет, Кетон"
    u"Я" "Привет, Василий!"
    k "Мы в игре?"
    show mks at center
    b "Да"
    k "Ты какой-то шакал"
    show mks smile at center with moveinright
    b "Ненавижу шутников"
    menu:
        b "Я даю тебе шанс решить свою судьбу"
        "Решить":
            "The end"
            $ ppoints += 2
        "Не решать":
            k "Я победил!!!"
            $ ppoints += 1
        "Что такое pass?":
            pass
    "???" "Тааак, понятно"
    b "Теперь протестим перемещния фоток"
    show mks at right
    show mks smile at left
    k "Шо?"
    hide mks with moveoutright
    k "Угу...."
    scene bg with fade
    show mks with moveinleft
    show mks with dissolve
    b "Теперь задник норм"
    scene bg
    show mks at left
    show mks smile at right
    with dissolve
    b "Теперь концовка"
    if ppoints == 2:
        b "Знал бы ты что ждало тебя на 1 поинте"
        centered "Поздравляем, вы пришли к лучшему окончанию!"
    elif ppoints == 1:
        b "/me растегнул ширинку"
        centered "Поздравляем, вы пришли к хорошему {b}окончанию{/b}."
    else:
        b "/me достал дилдон"
        centered "Нормальное окончание."
    return
## https://clck.ru/GaY2o
