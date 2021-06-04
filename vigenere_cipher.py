def check_key_len(key, msg_len):
    key_list = list(key)
    if msg_len > len(key):
        for i in range(msg_len - len(key)):
            key_list.append(key_list[i])
        return ''.join(key_list)
    elif msg_len < key:
        return key[:msg_len]
    else:
        return key


def space_pos(msg):
    space_position = []
    for i in range(len(msg)):
        if msg[i] == ' ':
            space_position.append(i)
    msg = msg.replace(' ', '')
    return msg, space_position


def space_insert(message, space_position):
    msg = list(message)
    for i in range(len(space_position)):
        msg.insert(space_position[i], ' ')
    final = ''.join(msg)
    return final


def vigenere_encryption(msg, key):

    en_msg_wo_space, en_space_position = space_pos(msg)
    msg_len = len(en_msg_wo_space)
    encryption_key = check_key_len(key, msg_len)
    cipher = []
    
    for enm, enk in zip(en_msg_wo_space, encryption_key):
       
        if enm.isupper():
            start = ord('A')
        else:
            start = ord('a')

        shift = ord(enm) - start
        pos = start + (ord(enk) - start + shift) % 26
        cipher.append(chr(pos))

    message = ''.join(cipher)
    encrypted_message = space_insert(message, en_space_position)
    print(encrypted_message)
    print("------------------------------------------------------")


def vigenere_decryption(msg, key):
    de_msg_wo_space, de_space_position = space_pos(msg)
    msg_len = len(de_msg_wo_space)
    decryption_key = check_key_len(key, msg_len)
    decipher = []
    
    for dem, dek in zip(de_msg_wo_space, decryption_key):
        
        if dem.isupper():
            start = ord('Z')
        else:
            start = ord('z')

        shift = abs(ord(dem) - start + 1)
        pos = start - (ord(dek) - start + shift) % 26
        decipher.append(chr(pos))
    
    message = ''.join(decipher)
    encrypted_message = space_insert(message, de_space_position)
    print(encrypted_message)
    print("------------------------------------------------------")


def main():
    print("------------------------------------------------------")
    print("|          VIGENERE ENCRYPTION AND DECRYPTION        |")
    print("------------------------------------------------------")
    print("")
    print("------------------------------------------------------")
    print("1) Vigenere Encryption\n2) Vigenere Decryption")
    print("------------------------------------------------------")
    option = str(input("Choose (1 or 2) >> "))
    print("------------------------------------------------------")
    message = input('Enter Message to be Encrypted/Decrypted: ')
    key = input('Enter Key for Encryption/Decryption: ')
    print("------------------------------------------------------")
    message = message
    key = key.lower()
    if option == '01' or option == '1':
        vigenere_encryption(message, key)
    elif option == '02' or option == '2':
        vigenere_decryption(message, key)


if __name__ == "__main__":
    main()
