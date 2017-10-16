import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.capitalize()
    if word in data:
        return data[word]
    elif w.lower() in data:
        return data[w.lower()]
    elif get_close_matches(word,data.keys(),cutoff=0.8).__len__()> 0:
        conf = input("Did you mean '" + get_close_matches(word,data.keys(),cutoff=0.8)[0] +"' instead? (Type y or n) : ")
        if conf.lower() == 'y':
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else :
        return "The word doesn't exist , Please double check"


word = input("Enter a word: ")

meaning =translate(word)

if type(meaning)== list:
    for i in meaning:
        print(i)
else:
    print(meaning)
