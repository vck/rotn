import string

letters = string.ascii_lowercase

letter2idx = {}
idx2letter = {}

for id, letter in enumerate(letters):
    letter2idx[letter] = id

for id, letter in enumerate(letters):
    idx2letter[id] = letter

def rot32(word, rot=32):
    chipered = ""
    for letter in word:
        id = letter2idx.get(letter)
        idx = (id+rot) % 26
        chipered += idx2letter.get(idx)
    return chipered

if __name__ == "__main__":
    print(rot32("hellot"))
    print(rot32("vernando"))
    for i in letters:
      print("{} ==> {}".format(i, rot32(i)))

