def clean_up(str):
    removeChars = ',.?!'
    for char in removeChars:
        str = str.replace(char, '')
    print(str.lower())
clean_up(input())


#print(str.lower().replace(',', '').replace('.', '').replace('?', '').replace('!', ''))
