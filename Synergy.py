print('Введите любую строку:')
string = input()
stringLength = len(string)

for i in range(0, stringLength // 2):
    if stringLength == 1 or (string[i] != string[stringLength - i - 1]):
        print('no')
        break
    if i == (stringLength // 2) - 1 :
        print('yes')