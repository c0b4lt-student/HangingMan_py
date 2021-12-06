import random


def count_line(fr_list):
    line_count = 0
    for line in fr_list:
        if line != '\n':
            line_count += 1
    fr_list.seek(0, 0)
    return line_count


def pick_word():
    fr_list = open("dictionary/fr_dict.txt", "r")
    line_count = count_line(fr_list)
    random_number = random.randint(1, line_count)
    i = 0
    while i < random_number:
        random_line = fr_list.readline()
        i += 1
    return random_line.lower().replace('\n', '')
