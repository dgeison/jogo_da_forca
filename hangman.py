import random

difficulty_levels = {
    '1': 'Fácil',
    '2': 'Médio',
    '3': 'Difícil'
}

words_lengths = {
    '1': (3, 5),
    '2': (6, 10),
    '3': (11, 1000)
}

print("A seguir escolha um nível de dificuldade: ")

difficulty_level = ''

while not difficulty_level:
    for k, v in difficulty_levels.items():
        print(f'{k} - {v.upper()}')

    difficulty_level = input("Escolha um nível de dificuldade: ")

    if difficulty_level not in difficulty_levels.keys():
        print("Nível inválido, tente novamente!")
        difficulty_level = ''


with open('static/words.txt', mode='r') as f_words:
    words = []
    for word in f_words.readlines():
        w = word.strip()
        min, max = words_lengths[difficulty_level]

        # if len(w) >= min and len(w) =< max:
        if min <= len(w) <= max:
            words.append(w)


max_index = len(words) - 1
random_index = random.randint(0, max_index)

selected_word = words[random_index]

print(selected_word)


total_attempts = 2 * len(selected_word)
if difficulty_level == '1':
    total_attempts += 2
elif difficulty_level == '3':
    total_attempts -= 2

print(f'Você tem {total_attempts} tentativas!')