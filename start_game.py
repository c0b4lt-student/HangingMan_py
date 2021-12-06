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


def make_guess(guessed_chars, random_word):
    is_new = False
    while not is_new:
        print("Veuillez entrer une lettre :")
        guess = input().lower()
        if len(guess) == 1 and not tabcnt(guessed_chars, guess) and guess.isalpha():
            guessed_chars.append(guess)
            if tabcnt(random_word, guess):
                return True
            is_new = True
    return False


def hide_word(clear_hidden_word, guessed_char):
    hidden_word = ''
    for char in clear_hidden_word:
        if tabcnt(guessed_char, char):
            hidden_word += char
        else:
            hidden_word += '*'
    return hidden_word


def draw_hangman(num_tries):
    print(" ____")
    print("|    |")
    print("|    %s" % ("O" if num_tries >= 1 else " "))
    print("|   %s%s%s" % (
        "/" if num_tries >= 3 else " ", "|" if num_tries >= 2 else " ", "\\" if num_tries >= 4 else " "))
    print("|   %s %s" % ("/" if num_tries >= 5 else " ", "\\" if num_tries >= 6 else " "))


def start_game():
    guessed_chars = [' ']
    tries = 0
    random_word = pick_word()
    hidden_word = hide_word(random_word, guessed_chars)
    print("Un mot secret à été choisi !")
    while not is_word_found(random_word, guessed_chars) and tries <= 6:
        print("Le mot secret est : %s" % hidden_word)
        if not make_guess(guessed_chars, random_word):
            draw_hangman(tries)
            tries += 1
        else:
            hidden_word = hide_word(random_word, guessed_chars)
    if tries > 6:
        print("Vous avez perdu le bon mot était %s" % random_word)
    else:
        print("Bien joué le mot était bien %s \n\n" % hidden_word)
