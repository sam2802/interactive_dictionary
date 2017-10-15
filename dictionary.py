import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else :
        w=get_close_matches(word,data.keys())[0]
        if w.__len__() > 0:
            return "Did you mean " + w
        else :
            return "The word doesn't exist , Please double check"


word = input("Enter a word: ").lower()

print (translate(word))
