from start_game import start_game

if __name__ == '__main__':
    if not run_tests():
        return False
    print("Petite partie de pendu ? (oui/non)")
    still_playing = input()
    while still_playing.lower() == 'o' or still_playing.lower() == 'oui':
        start_game()
        print("Petite partie de pendu ? (oui/non)")
        still_playing = input()
