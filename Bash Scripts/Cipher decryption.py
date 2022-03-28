import math
​
moves = [3,4,1,2,5,6]
msg = "u Yocanen vecar tcthh e phAlab Betant,di Mney xtar Tgeist  Cvialnsou Hse"
​
decrypted = list(msg)
​
for i, letter in enumerate(msg):
    moves_index = i % len(moves)
​
    index = (math.floor(i / len(moves)) * len(moves)) + moves[moves_index]
​
    decrypted[index - 1] = letter
​
    print(str.format('{}, at index {}, goes in destination index {} (letter number {})', letter, i, index - 1, index))
​
print(''.join(decrypted))