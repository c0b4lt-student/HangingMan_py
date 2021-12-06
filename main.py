from start_game import start_game
from tests.run_tests import run_tests

if __name__ == '__main__':
    if not run_tests():
        exit(84)
    print("Petite partie de pendu ? (oui/non)")
    still_playing = input()
    while still_playing.lower() == 'o' or still_playing.lower() == 'oui' or still_playing.lower() == 'uiii':
        start_game()
        print("Petite partie de pendu ? (oui/non)")
        still_playing = input()
