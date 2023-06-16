from utils import show_difficult_menu
from utils import get_random_word
from utils import play_hangman


if __name__ == "__main__":
    difficulty_level = show_difficult_menu()
    selected_word = get_random_word(difficulty_level=difficulty_level)
    player_wins = play_hangman(
        selected_word=selected_word, difficulty_level=difficulty_level
    )

    if player_wins:
        print("Parabéns, você venceu!")
    else:
        print("Que pena, você perdeu!")

    print(f"A palavra era: {selected_word}")
