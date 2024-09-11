# Vigenère cipher -- the offset for each letter is determined by another text, called the key. --

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append space to the message
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
            
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

encryption = encrypt(text, custom_key)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
print(f'\nEncryption Successful: {encryption}')