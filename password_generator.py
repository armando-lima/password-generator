import random
import string


CHAR_MAP = {
    'uppercase': string.ascii_uppercase,
    'lowercase': string.ascii_lowercase,
    'numbers': string.digits,
    'special_characters': string.punctuation,
}


#Generates a random password but you cannot select which type of characters you want
def generate_0(length):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    #for blank into range from 0 to lenght (inclusive, exclusive)
    for _ in range(length):
        #adds a random choice from chars pool to password
        password += random.choice(chars)
    print(password)


#Generates a random password but it has a lot of redundant code
def generate_1(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''

    if uppercase:
        chars += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)
    
    if lowercase:
        chars += string.ascii_lowercase
        password += random.choice(string.ascii_lowercase)

    if numbers:
        chars += string.digits
        password += random.choice(string.digits)

    if special_characters:
        chars += string.punctuation
        password += random.choice(string.punctuation)

    for _ in range(length - len(password)):
        password += random.choice(chars)
    
    random.shuffle(password)
    #Converting a list to a string using join
    password = ''.join(password)

    print(password)


def generate_2(length, uppercase=True, lowercase=True, numbers=True, special_characters=True):
    password = []
    chars = ''
    
    for key, value in CHAR_MAP.items():
        if locals()[key]:
            chars += value
            password += random.choice(chars)

    for _ in range(length - len(password)):
        password += random.choice(chars)
    
    random.shuffle(password)
    password = ''.join(password)

    print(password)


#*args - arguments
#**kwargs - keyword arguments
#it enables the function to receive any number of non named arguments
def generate(length, **kwargs): #putting "pass" means don't do anything | kwargs upacks things, also means keyword arguements | *args means arguements
    password = []
    chars = ''

    if not any(kwargs.values()):
        return 'Please provide at least one password requirement' #error handling

    for item in kwargs:
        if kwargs[item] and CHAR_MAP.get(item):
            chars += CHAR_MAP[item]
            password += random.choice(CHAR_MAP[item]) #doing the 1st "if" statements above

    for _ in range(length - len(password)):
        password += random.choice(chars)

    random.shuffle(password)
    return ''.join(password) 


if __name__ == '__main__':
    print(generate(25, uppercase=True))