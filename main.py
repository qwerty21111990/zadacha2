def polindrom(string):
    string = string.lower()
#    wrong = [',', '.', '-', '?', '!', ':']
#    for symbol in wrong:
#        string = string.replace(symbol, '')
    return string == string[::-1]


string = input()
print(polindrom(string))

