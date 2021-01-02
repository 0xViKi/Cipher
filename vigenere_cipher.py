# ██    ██ ██  ██████  ███████ ███    ██ ███████ ██████  ███████      ██████ ██ ██████  ██   ██ ███████ ██████
# ██    ██ ██ ██       ██      ████   ██ ██      ██   ██ ██          ██      ██ ██   ██ ██   ██ ██      ██   ██
# ██    ██ ██ ██   ███ █████   ██ ██  ██ █████   ██████  █████       ██      ██ ██████  ███████ █████   ██████
#  ██  ██  ██ ██    ██ ██      ██  ██ ██ ██      ██   ██ ██          ██      ██ ██      ██   ██ ██      ██   ██
#   ████   ██  ██████  ███████ ██   ████ ███████ ██   ██ ███████      ██████ ██ ██      ██   ██ ███████ ██   ██


def vig_encryption(a, b):
    k = []
    cipher_num = []
    encrypt_text = []
    space = []

    for i in range(len(a)):
        if a[i] == ' ':
            space.append(i)

    a = a.replace(' ', '')
    a = list(a.lower())
    b = list(b.lower())

    if (len(b) < len(a)):
        for i in range(len(a) - len(b)):
            b.append(b[i])
    elif (len(b) > len(a)):
        b = b[:len(a)]

    for i, j in zip(a, b):
        numa = ord(i) - 96
        numb = ord(j) - 96
        k.append(numa + numb)

    for i in k:
        cipher_num.append(i % 26)

    for n, t in enumerate(cipher_num):
        if t == 0:
            cipher_num[n] = 1
        if t == 1:
            cipher_num[n] = 26
        elif t < 26:
            cipher_num[n] = cipher_num[n] - 1

    for i in range(len(cipher_num)):
        encrypt_text.append(chr(cipher_num[i] + 96))

    for i in range(len(space)):
        encrypt_text.insert(space[i], " ")

    m = ''.join(encrypt_text)
    return m.upper()


def vig_decryption(a, b):
    k = []
    decipher_num = []
    decrypt_text = []
    space = []
    for i in range(len(a)):
        if (a[i] == ' '):
            space.append(i)

    a = a.replace(' ', '')
    a = list(a.lower())
    b = list(b.lower())

    if (len(b) < len(a)):
        for i in range(len(a) - len(b)):
            b.append(b[i])
    elif (len(b) > len(a)):
        b = b[:len(a)]

    for i, j in zip(a, b):
        numa = ord(i) + 96
        numb = ord(j) + 96
        k.append(numa - numb + 26)

    for i in k:
        decipher_num.append(i % 26)

    for n, t in enumerate(decipher_num):
        if t == 0:
            decipher_num[n] = 1
        if t == 1:
            decipher_num[n] = 26
        elif t < 26:
            decipher_num[n] = decipher_num[n] + 1

    for i in range(len(decipher_num)):
        decrypt_text.append(chr(decipher_num[i] + 96))

    for i in range(len(space)):
        encrypt_text.insert(space[i], " ")

    m = ''.join(decrypt_text)

    return m.upper()


def take_input():
    print("1 => Encrypt Text")
    print("2 => Decrypt Text")
    val = int(input("Choose Option: "))
    if val == 1:
        a = input('\nEnter Plain Text: ')
        b = input('Enter the encryption key: ')
        res = vig_encryption(a, b)
        print(f"\nEncrypted Text: {res}")

    elif val == 2:
        a = input('\nEnter Encrypted Text: ')
        b = input('Enter the encryption key: ')
        res = vig_decryption(a, b)
        print(f"\nDecrypted Text: {res}")
    else:
        print('\n')
        take_input()


def main():
    print(
        '''
   _  _ _ ____ ____ _  _ ____ ____ ____    ____ _ ___  _  _ ____ ____
   |  | | | __ |___ |\ | |___ |__/ |___    |    | |__] |__| |___ |__/
    \/  | |__] |___ | \| |___ |  \ |___    |___ | |    |  | |___ |  \_

    '''
    )
    take_input()


if __name__ == "__main__":
    main()
