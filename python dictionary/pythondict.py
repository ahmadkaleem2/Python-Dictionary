import json
import difflib
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    word_cap  = word.title()

    if word in data:
        return data[word][0]
    elif word_cap in data:
        return data[word_cap][0]

    else:

        if len(difflib.get_close_matches(word,data))==1:

            if input(f"did you mean? + {difflib.get_close_matches(word,data)}").lower()=="yes":
                print('asdasd')
                return data[difflib.get_close_matches(word,data)[0]]




        elif len(difflib.get_close_matches(word,data))>=2:

            print(f"did you mean? + {difflib.get_close_matches(word,data)}")
            choice = int(input("select index of word"))

            if choice<len(difflib.get_close_matches(word,data)) and choice>-1:
                return data[difflib.get_close_matches(word,data)[choice]]


        else:
            return "doesn't exist"



Input = input("Enter Word")
print(translate(Input))


print(data.keys())





