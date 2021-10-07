'''take1'''

dict = {'a': 1, 'b': 2, 'c': 3, ' ': '-'}

input = "acb bac" #here goes the data you want to encrypt

decode = ""

for letters in input:
    decode = f'{decode} {str(dict[letters])}'

print(decode)