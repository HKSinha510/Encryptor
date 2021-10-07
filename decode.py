dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z', '-': ' ', ' ': ''}

input = '14 5 22 5 18 - 7 15 14 14 1 - 7 9 22 5 - 25 15 21 - 21 16' #here goes your encrypted data
slice = input.split(" ")
decoded = ""

for letters in slice:
    decoded += str(dict[letters])

print(decoded)