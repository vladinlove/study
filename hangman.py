# Виселица
#
# Классическая игра. Компьютер выбирает слово
# и игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за определенное количество попыток, на экране появится фигурка повешенного.

# Импорт модуля
import random

# константы
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("КОШКА", "СОБАКА", "ГРЕЙПФРУТ", "БАНАН", "БАРБАРИС")

# инициализация переменных
word = random.choice(WORDS)   # слово для отгадывания
so_far = "-" * len(word)      # по одному дефису на каждую букву, которую надо отгадать
wrong = 0                     # число ошибок
used = []                     # предложенные буквы


print("Добро пожаловать в Вислецу. Удачи!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong]) #вид виселецы
    print("\nВы уже предлагали эти буквы:\n", used) #список использованных букв
    print("\nОтгаданное вами сейчас выглядит так:\n", so_far) #отгаданное на данный момент

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    
    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("Введите букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nДа! Буква ", guess, " есть в слове!")

        # новая строка с отгаданной буквой/буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]              
        so_far = new

    else:
        print("\К сожалению, буквы ", guess, " нет в слове.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы угадали!")
    
print("\nБыло загадано слово", word)

input("\n\nPress the enter key to exit.")