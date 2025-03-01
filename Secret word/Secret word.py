# Programed by: Joy 

import random
import string

#Encoding Text
def encode_word(word):
    if len(word) >= 3:
        # Remove the first letter and append it to the end
        encoded_word = word[1:] + word[0]

        # Add random characters at the beginning and end
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        encoded_word = random_chars + encoded_word + random_chars

        return encoded_word
    else:
        # Reverse the word if it's less than 3 letters
        return word[::-1]

def encode_sentence(sentence):
    words = sentence.split()
    encoded_words = []

    for word in words:
        encoded_word = encode_word(word)
        encoded_words.append(encoded_word)

    return ' '.join(encoded_words)

# Decoding Text
def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        # Remove 3 letters from the start and end
        word = word[3:-3]

        if len(word) > 0:
        
            word = word[-1] + word[:-1]

        return word

def decode_sentence(sentence):
    words = sentence.split()
    decoded_words = []

    for word in words:
        decoded_word = decode_word(word)
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)

# Asking for Encoding/Decoding
def main():
    choice = input("Do you want to encode or decode the text? (encode/decode): ").strip().lower()

    if choice == "encode":
        sentence = input("Enter a text to encode: ")
        encoded_sentence = encode_sentence(sentence)
        print("Encoded Text:", encoded_sentence)
    elif choice == "decode":
        sentence = input("Enter a text to decode: ")
        decoded_sentence = decode_sentence(sentence)
        print("Decoded Text:", decoded_sentence)
    else:
        print("Invalid choice. Please choose 'encode' or 'decode'.")

if __name__ == "__main__":
    main()