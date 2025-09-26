# d = {'a':1,'b':{"c":"data"},"d":2,"e":["f","g"]}

d = eval(input("Enter the Dictionary: "))

for key in d:
    print(key, end = " ")

    if type(d[key]) == dict:
        for subkey in d[key]:
            print(subkey, end = " ")

    if type(d[key]) == list:
        for subkey in d[key]:
            print(subkey, end = " ") 