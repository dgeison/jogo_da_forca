import re
from utils import show_difficult_menu, get_random_word, get_total_attempts


difficulty_level = show_difficult_menu()
selected_word = get_random_word(difficulty_level=difficulty_level)
total_attempts = get_total_attempts(selected_word, difficulty_level)
available_attempts = total_attempts

print(f"A quantidade de chances para acertar a palavra é: {total_attempts}")

current_state = ["_" for letter in selected_word]
guessed_letters = []

while "_" in current_state and available_attempts:
    print(
        f"\n\n### Tentativa número: {total_attempts - available_attempts + 1} de {total_attempts}###"
    )
    for char in current_state:
        print(char, end=" ")

    guess = ""

    while not guess:
        guess = input("\nDigite uma letra: ").lower()
        if len(guess) != 1 and not re.match("[a-z]", guess):
            print("Entrada inválida. Tente novamente, entrando apenas 1 letra.")
            guess = ""

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess in selected_word:
            pass
        positions = []
        index = 0
        for letter in selected_word:
            if letter == guess:
                positions.append(index)
            index += 1

        for index in positions:
            current_state[index] = guess

        else:
            available_attempts -= 1

    else:
        print("Você já tentou essa letra!")
