def ceasar_encrypt(message, k):
    res = ''
    for i in message:
        t = ord(i)
        res += chr(((t - 97 + k) % 26) + 97)
    return res

def ceasar_decrypt(code, k):
    res = ''
    for i in message:
        t = ord(i)
        res += chr((abs(t - k) % 26) + 97)
    print(res)

if __name__ == '__main__':
    message = input('Enter your mesasage: ')
    k = int(input('k = '))
    encode = ceasar_encrypt(message, k)
    print(encode)
