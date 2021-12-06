from start_game import is_word_found


def is_word_found_test():
    if not is_word_found("Hello World", 'Helo Wrd'):
        print("Erreur is_word_found(\"Hello World\", \"Helo Wrd\") == False")
        return False
    if not is_word_found("", ''):
        print("Erreur is_word_found(\"\", \'\') == False")
        return False
    if is_word_found("Hello World", "Helo Wor"):
        print("Erreur is word_found(\"\") == True")
    return True
