import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word= word.lower() ## shrey
    if word in data:
        return data[word]
    elif word.title() in data: ## Shrey
        return data[word.title()]
    elif word.upper() in data: ## SHREY
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys()))>0:  ## by using a get close matches package from difflib it will help to recognize any relatable word if user enter a little wrong word in dictionary
        print("Did yiu mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("Press y for yes and n for no")
        if decide =='y':
            return data[get_close_matches(word , data.keys())[0]]
        elif decide =='n':
            return ("Oops! Wrong word")
        else:
            return("Entered wrong input")
    else:
        print("Oops! Wrong word")

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:## if we only use for loop and we have a one word meaning it will divide word in one alphabet and print it so use if else
    for item in output:  ## to print line by line for better understanding
        print(item)
else:
    print(output)

