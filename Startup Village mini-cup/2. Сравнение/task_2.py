def to_int(string):
    result = 0
    l = len(string)
    for i, s in enumerate(string):
        if  i + 1 < l and dictionary[s] < dictionary[string[i+1]]:
            result -= dictionary[s]
        else:
            result += dictionary[s]
    return result

dictionary = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

roman1, roman2 = map(to_int, input().split())
if roman1 > roman2:
    print('1')
elif roman1 < roman2:
    print('-1')
else:
    print('0')