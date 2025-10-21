import random
info = ("Губка Боб", 3)

player = {
    "name": info[0],
    "lives": info[1],
    "score": 0
}

hints = [
    "Подумай о друзьях Губки Боба!",
    "Вспомни, где он работает!",
    "Ты можешь это сделать!",
    "Не сдавайся!"
]

items = set()

levels = {  
    1: {
        "question": "Кто лучший друг Губки Боба?",
        "answer": "патрик"
    },
    2: {
        "question": "Где работает Губка Боб?",
        "answer": "красти краб"
    }
}

def show_status():
    print()
    print("Имя:", player["name"])
    print("Жизни:", player["lives"])
    print("Очки:", player["score"])
    if len(items) == 0:
        print("Предметы: нет")
    else:
        print("Предметы:", ", ".join(items))
    print("-" * 35)

def ask_question(level):
    print()
    print("Уровень", level)
    print("Вопрос:", levels[level]["question"])
    answer = input("Твой ответ: ").lower().strip()

    if answer == levels[level]["answer"]:
        print(" Правильно!")
        player["score"] += 5
        items.add("Приз уровня " + str(level))
    else:
        print(" Неправильно!")
        player["lives"] -= 1
        print("Подсказка:", hints[level - 1])

def random_event():
    print()
    print("Случайное событие...")
    number = random.randint(1, 3)
    if number == 1:
        print("Ты нашёл пузырь счастья! +1 очко")
        player["score"] += 1
        items.add("Пузырь счастья")
    elif number == 2:
        print("Ты поскользнулся на водорослях! -1 жизнь")
        player["lives"] -= 1
    else:
        print("Ты нашёл морскую звезду! +2 очка")
        player["score"] += 2
        items.add("Морская звезда")

def mini_game():
    print()
    print("Мини-игра: угадай число от 1 до 3")
    secret = random.randint(1, 3)
    guess = input("Твой вариант: ")

    if guess.isdigit() and int(guess) == secret:
        print(" Угадал! +3 очка")
        player["score"] += 3
        items.add("Счастливое число")
    else:
        print("Не угадал!")
        player["lives"] -= 1

def play_level(level):
    ask_question(level)

    if player["lives"] <= 0:
        return

    random_event()

    if player["lives"] <= 0:
        return

    mini_game()

    if player["lives"] <= 0:
        return

    show_status()

def ending():
    print()
    print("Конец игры!")
    print("Очки:", player["score"])
    print("Предметы:", ", ".join(items))
    if player["score"] >= 10:
        print("Ты настоящий герой Бикини Боттом!")
    else:
        print("Ты немного устал, но справился!")


def main():
    print("Добро пожаловать в игру 'Губка Боб: Головоломка'")
    print("Отгадай загадки, получай очки и не теряй жизни!")
    show_status()

    for level in range(1, 3):
        if player["lives"] <= 0:
            break
        play_level(level)

    if player["lives"] > 0:
        ending()
    else:
        print()
        print("Увы, Губка Боб проиграл...")
        print("Попробуй снова!")


if __name__ == "__main__":
    main()

