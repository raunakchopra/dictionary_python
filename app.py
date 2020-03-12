import json 
data = json.load(open("data.json"))

import difflib
from difflib import get_close_matches

def meaning(word):
    word = word.lower()
    if(word in data):
        for meaning in data[word]:
            print(meaning)
    elif(len(get_close_matches(word,data.keys()))>0):
        print('Did you mean ',get_close_matches(word,data.keys())[0],'?')
        choice=input()
        if(choice == 'y'):
            word=get_close_matches(word,data.keys())[0]
            for meaning in data[word]:
                print(meaning)
    else:
        print('Word does not exist. Please Double Check your word.')
        main()

def main():
    word = input('Input the word: ')
    meaning(word)

main()