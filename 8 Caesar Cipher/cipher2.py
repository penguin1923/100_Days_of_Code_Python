import cipher_alphabet
import cipher_art

print(cipher_art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_index = []
new_word = []

def encrypt(texts,shifts):
    for letter in texts:
        text_index.append(letter)

    for input in text_index:
        index1 = cipher_alphabet.alphabet.index(input)

        if (index1 + shifts)<=25:
            index2 = cipher_alphabet.alphabet[index1 + shifts]
            new_word.append(index2)
        else:
            index2 = cipher_alphabet.alphabet[(index1 + shifts)-26]
            new_word.append(index2)
encrypt(texts=text,shifts=shift)

joined_new_word = "".join(new_word)
print(f"The encoded text is {joined_new_word}")
