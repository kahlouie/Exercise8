import random
from sys import argv
script, filename1, filename2 = argv

def read_text(text, text2):
    f = open(text)
    r = open(text2)
    text = f.read() + r.read()
    return text

def strip_text(text):
    sexy_list = text.split()
    for i in range(len(sexy_list)):
        sexy_list[i] = sexy_list[i].strip("\"\'")
    return sexy_list

def tuple_dict(l):
    bigram_dict = {}
    for i in range(len(l) - 2):
        tuple_var = (l[i], l[i + 1])
        if not bigram_dict.get(tuple_var):
            bigram_dict[tuple_var] = [l[i + 2]]
        else:
            bigram_dict[tuple_var].append(l[i + 2])
    return bigram_dict

def make_pseudo_text(dict):
    caplist = []
    for i in dict.keys():
        current_tuple = i[0]
        first_letter_caps = ord(current_tuple[0])
        ASCII_A = ord("A")
        ASCII_Z = ord("Z")
        main_characters = ["Harry", "Hermione", "Ginny", "Ron", "Dumbledore", "Snape", "Malfoy"]
        if i[0] != "" and i[1] != "" and (i[0] in main_characters or i[1] in main_characters):
            if first_letter_caps >= ASCII_A and first_letter_caps <= ASCII_Z:
                caplist.append(i)
    new_words = random.sample(caplist, 1)
    new_words = new_words[0]
    pseudo_text = new_words[0] + " " + new_words[1]
    while len(pseudo_text) <= 100:
        next_word = random.sample(dict.get(new_words), 1)
        pseudo_text += " " + next_word[0]
        new_words = new_words[1], next_word[0]
    return pseudo_text

def main():

    text = read_text(filename1, filename2)
    _list = strip_text(text)
    bigram_dict = tuple_dict(_list)
    final_output = make_pseudo_text(bigram_dict)
    print "..." + final_output + "..."



main()