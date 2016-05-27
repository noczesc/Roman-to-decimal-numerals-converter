roman = input("Give me a roman numeral and I'll convert it to decimal for you ->>>")

addlist = [1000, 500, 100, 50, 10, 5, 1]
sublist = [-100, -100, -10, -10, -1, -1]
romanaddlist = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
romansublist = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']

add = []
subtract = []

for i in range(len(roman)):
    cas = roman[i:i + 1]  # currentaddslice
    for index, z in enumerate(romanaddlist):
        if romanaddlist[index] == cas:
            add.append(addlist[index])

    css = roman[i:i + 2]  # currentsubtractslice
    for index, e in enumerate(romansublist):
        if romansublist[index] == css:
            subtract.append(sublist[index])

else:
    realnumber = sum(add) + sum(subtract)*2
    print("Your number is " + str(realnumber) + " in decimal")
