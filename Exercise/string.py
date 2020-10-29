# -------------------- Str----------------
# slicing
a = "Hello, World Hype!"
# print(a[1:5])
# print(len(a))
# print(a.split(","))
# print(a.strip()) # returns "Hello, World!"
# print(a.lower())
# print(a.upper())
# print(a.replace("H", "J"))

# txt = "The rain in Spain stays mainly in the plain"
# x = "ain" not in txt
# print(x)

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
        # print(keys)
    return dict
# print char_frequency('nahid.google.com')

def not_poor (str):
    str1 = str.find('not')
    str2 = str.find('poor')
    # print(str1)
    if str2 > str1 and str1 > 0 and str2 > 0:
        str = str.replace(str[str1:(str2+4)],'good')
        return str
    else:
        return str
    
# print(not_poor('the lyrics is not poor song'))

def find_longest_word(word_list):
    word_len = []
    for i in word_list:
        word_len.append((len(i),i))
    word_len.sort()
    # print(type(word_len))
    return word_len[-1][1]

# print(find_longest_word(["PHP", "Exercises", "Backend","book"]))


