import random
from constants import WORDS_LENGTHS, DIFFICULTY_LEVELS


def show_difficult_menu():
    """
    Exibe o menu que permite o jogador selecionar o nível de dificuldade

    :return: difficulty_level
    """
    print("A seguir escolha um nível de dificuldade: ")

    difficulty_level = ""

    while not difficulty_level:
        for k, v in DIFFICULTY_LEVELS.items():
            print(f"{k} - {v.upper()}")

        difficulty_level = input("Escolha um nível de dificuldade: ")

        if difficulty_level not in DIFFICULTY_LEVELS.keys():
            print("Nível inválido, tente novamente!")
            difficulty_level = ""

    return difficulty_level


def get_random_word(difficulty_level):
    """
    Retorna uma palavra aleatória do arquivo words.txt

    :param difficulty_level: nível de dificuldade selecionado pelo jogador

    :return: selected_word
    """
    with open("static/words.txt", mode="r", encoding="utf-8") as f_words:
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
    print(f"A palavra selecionada foi: {selected_word}")
    return selected_word


def get_total_attempts(selected_word, difficulty_level):
    """
    Retorna o total de tentativas que o jogador terá para acertar a palavra.

    :param selected_word: palavra selecionada aleatoriamente
    :param difficulty_level: nível de dificuldade selecionado pelo jogador

    :return: total_attempts
    """
    unique_letters = set(selected_word)
    total_attempts = 1.5 * len(unique_letters)
    if difficulty_level == "1":
        total_attempts += 2
    elif difficulty_level == "3":
        total_attempts -= 2
        total_attempts = min([total_attempts, 18])

    total_attempts = round(total_attempts)
    return total_attempts
