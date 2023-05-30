# function will convert string parameter to upper case
def to_upper(str: str):
    try:
        for i in str:
            if str == str:
                return str.upper()
    except TypeError:
            print("TypeError: Wrong attribute")

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list: list):
    try:
        for word in str_list:
            if word.islower():
                    return False
        return True
    except TypeError:
            print("TypeError: Wrong attribute")


print(to_upper(1))
print(to_word_list_isupper(2))