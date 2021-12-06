from pick_word import pick_word


def tabcnt(tab, elem):
    for e in tab:
        if e == elem:
            return True
    return False


def is_word_found(random_word, guessed_chars):
    for e in random_word:
        if not tabcnt(guessed_chars, e):
            return False
    return True


def make_guess(guessed_chars):
    is_new = False
    while not is_new:
        print("Veuillez entrer une lettre :")
        guess = input().lower()
        if len(guess) == 1 and not tabcnt(guess, guessed_chars):
            is_new = True


def start_game():
    guessed_chars = [' ']
    tries = 0
    random_word = pick_word()
    print("Un mot secret à été choisi !")
    while not is_word_found(random_word, guessed_chars) and tries < 6:
        make_guess(guessed_chars)
        tries += 1
