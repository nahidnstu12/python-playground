def sentence_maker (phrase):
    interogative = ('what','why','when','how')

    capitalized = phrase.capitalize()

    if(phrase.startswith(interogative)):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

# print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say Something: ")

    if(user_input == "/end"):
        break
    else:
        results.append(sentence_maker(user_input))

# print(results)
print(" ".join(results))