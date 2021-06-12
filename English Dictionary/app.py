import json
from difflib import get_close_matches

# data = json.load(open("English Dictionary/data.json"))
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    matches = get_close_matches(w,data.keys())

    if w in data:
        return data[w]
    elif len(matches) > 0 :
        yn =input("Did you mean %s instaed?If yes,type Y otherwise N: " % matches[0])
        if yn == "Y":
            return data[matches[0]]
        elif yn == "N":
            return "The word doesn't exist.Please double check"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check"


word = input("Enter word: ")   

# print(translate(word))

output = translate(word)

if type(output) == list:
    for lines in output:
        print(lines)
else:
    print(output)