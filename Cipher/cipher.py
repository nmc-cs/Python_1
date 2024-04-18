def encode(message, encoding_dict):
    # Check if each character in the message is present in the encoding dictionary
    for ele in message:
        if ele not in encoding_dict.keys():
            # If a character is not found in the encoding dictionary, return the original message
            return message

    # Replace elements with the appropriate dictionary keys
    for key, value in encoding_dict.items():
        message = message.replace(key, value)
    return message


def decode(message, encoding_dict):
    # Check if each character in the message is present in the values of the encoding dictionary
    for ele in message:
        if ele not in encoding_dict.values():
            # If a character is not found in the values of the encoding dictionary, return the original message
            return message

    # Replace elements with the appropriate dictionary keys
    for key, value in encoding_dict.items():
        message = message.replace(value, key)
    return message

# Cipher set
encoding_dict = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5',
                 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '!', 'l': '@', 'm': '#', 'n': '$',
                 'o': '%', 'p': '^', 'q': '&', 'r': '*', 's': '(', 't': ')', 'u': '-', 'v': '+',
                 'w': '<', 'x': '>', 'y': '?', 'z': '=', " ": " "}

while 1:
    print("Welcome to the Secret Message Encoder/Decoder")
    print("1. Encode a message\n2. Decode a message\n3. Exit")

    while 1:
        n = input("What would you like to do? ")
        if not n.isdigit():
            print("Please enter a number between 1 and 3.")
            continue
        if n < '1' or n > '3':
            print(n, ' is not a valid choice.')
        else:
            n = int(n)
            break
    if n == 1:
        encode_message = input('Enter a message to encode: ')
        print('Encoded message:', encode(encode_message, encoding_dict))
    elif n == 2:
        decode_message = input('Enter a message to decode: ')
        print('Encoded message:', decode(decode_message, encoding_dict))
    else:
        break
