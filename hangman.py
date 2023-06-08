import random
from constants import WORDS_LENGTHS, DIFFICULTY_LEVELS


def show_difficult_menu():
    """Show the difficult menu"""
    print("A seguir escolha um nível de dificuldade: ")

    difficulty_level = ''

    while not difficulty_level:
        for k, v in DIFFICULTY_LEVELS.items():
            print(f'{k} - {v.upper()}')
        difficulty_level = input("Escolha um nível de dificuldade: ")

        if difficulty_level not in DIFFICULTY_LEVELS.items():
            print("Nível inválido, tente novamente!")
            difficulty_level = ''
    return difficulty_level


def get_random_word(difficulty_level):
    """Get a random word from a file"""
    with open('static/words.txt', mode='r', encoding='utf-8') as f_words:
        words = []
        for word in f_words.readlines():
            w = word.strip()
            min, max = WORDS_LENGTHS[difficulty_level]

            # if len(w) >= min and len(w) =< max:
            if min <= len(w) <= max:
                words.append(w)

    max_index = len(words) - 1
    random_index = random.randint(0, max_index)

    selected_word = words[random_index]

    print(selected_word)
    return selected_word


def get_total_attempts(selected_word, difficulty_level):
    """Return the total attempts based on the difficulty level"""
    total_attempts = 2 * len(selected_word)
    if difficulty_level == '1':
        total_attempts += 2
    elif difficulty_level == '3':
        total_attempts -= 2

    print(f'Você tem {total_attempts} tentativas!')
