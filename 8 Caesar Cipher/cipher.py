import cipher_alphabet
import cipher_art

print(cipher_art.logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    text_index = []
    new_word = []

    def caesar(text_input,shift_count,cipher_direction):
        for letter in text_input:
            text_index.append(letter)

        for char in text_index:
            if char in cipher_alphabet.alphabet:

                index_number = cipher_alphabet.alphabet.index(char)

                if cipher_direction == "encode":
                    index_letter = cipher_alphabet.alphabet[(index_number + shift_count) % 26]
                    new_word.append(index_letter)
                elif cipher_direction == "decode":
                    index_letter = cipher_alphabet.alphabet[(index_number - shift_count) % 26]
                    new_word.append(index_letter)
                else:
                    continue
            else:
                new_word.append(char)

        joined_new_word = "".join(new_word)

        if cipher_direction == "encode" or "decode":
            print(f"The {cipher_direction}d text is {joined_new_word}")
        else:
            print("That was not a valid option.")

    caesar(text_input=text,shift_count=shift,cipher_direction=direction)
    result = input("Type 'yes' if you would like to run the Caesar Cipher again? Otherwise type 'no'.\n ")
    if result == "yes":
        should_continue = True
    elif result == "no":
        should_continue = False
        print("Goodbye")
    else:
        should_continue = False
        print("Invalid response.... Terminating")
