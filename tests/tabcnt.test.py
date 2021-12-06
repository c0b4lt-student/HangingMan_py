from start_game import tabcnt


def tabcnt_test():
    if not tabcnt([1, 4, 9], 1):
        return False
    if tabcnt([1, 4, 9], 5):
        return False
    if not tabcnt("Salut", 'S'):
        return False
    if not tabcnt(["Salut", "tout", "le", "monde"], 'tout'):
        return False
    return True
