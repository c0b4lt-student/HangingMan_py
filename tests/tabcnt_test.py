from start_game import tabcnt


def tabcnt_test():
    if not tabcnt([1, 4, 9], 1):
        print ("Erreur tabcnt.test([1, 4, 9], 1)")
        return False
    if tabcnt([1, 4, 9], 5):
        print ("Erreur tabcnt.test([1, 4, 9], 5)")
        return False
    if not tabcnt("Salut", 'S'):
        print("Erreur tabcnt.test(\"Salut\", \'S\')")
        return False
    if not tabcnt(["Salut", "tout", "le", "monde"], 'tout'):
        print("Erreur tabcnt.test([\"Salut\", \"tout\", \"le\", \"monde\"], \'tout\')")
        return False
    return True
