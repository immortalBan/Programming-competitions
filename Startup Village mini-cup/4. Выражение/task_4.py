dictionary = {
    "&": "and",
    "|": "or",
    "!": "not",
    "=": "=="
    }

equation, *values = input().split()
equation = '(' + equation + ')'
equation = equation.replace('=', ')=(')

equation = ' '.join(list(equation))

for i in range(0, len(values), 2):
    dictionary[values[i]] = values[i+1]

equation = equation.split()
for i in range(len(equation)):
    if equation[i] in dictionary: 
        equation[i] = dictionary[equation[i]]

equation = ' '.join(equation)

print(eval(equation))