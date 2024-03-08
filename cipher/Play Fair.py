"""
VD:
Cho M = HELLOONEANDALL
K = THEDIEIS
Bảng chữ cái: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

GIẢI:
+ Key sẽ là ma trận 5x5 như sau:(i, j được đặt cùng 1 vị trí do có 26 chữ cái mà chỉ có 25 ô)
T H E D I,J
S A B C F
G K L M N
O P Q R U
V W X Y Z

+ Tách message theo cặp 2 chữ cái, nếu 2 chữ cái trùng nhau thì thêm 'X' vào giữa, nếu số ký tự lẻ thêm 'X' vào cuối
M = HE LX LO ON EA ND AL LX

+ Mã hoá theo từng cặp
    + Nếu 2 ký tự cùng một hàng thì dịch phải 1 đơn vị, nếu ký tự ở cột cuối cùng thì chuyển sang trái
    + Nếu cùng một hàng thì dịch xuống 1 đơn vị, nếu ký tự ở hàng cuối thì chuyển lên đầu
    + Nếu tạo thành 1 hình chéo hình chữ nhật thì mã hoá thành đường chép còn lại, lấy theo thứ tự cùng hàng
C = ED QE GQ UG HB MI BK QE
"""


def unique_chars(input_str):
    seen = set()
    res = ''
    for char in input_str:
        if char not in seen:
            res += char
            seen.add(char)
    return res


def generate_key_matrix(key):
    matrix = [[None] * 5 for _ in range(5)]
    alpabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.replace(' ', '').upper()
    key += alpabet
    key = unique_chars(key)
    for i in range(5):
        for j in range(5):
            matrix[i][j] = key[5 * i + j]
    return matrix


def play_fair_encrypt(message, key_str):
    key = generate_key_matrix(key_str)

    def find_position(char):
        for i in range(5):
            for j in range(5):
                if char == key[i][j]:
                    return i, j

    res = ''
    message = message.replace('J', 'I').upper()
    message = message.replace(' ', '')
    for i in range(0, len(message), 2):
        if message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
    if len(message) % 2 == 1:
        message += 'X'
    for i in range(0, len(message), 2):
        i1, j1 = find_position(message[i])
        i2, j2 = find_position(message[i + 1])
        if i1 == i2:
            res += key[i1][(j1 + 1) % 5] + key[i2][(j2 + 1) % 5]
        elif j1 == j2:
            res += key[(i1 + 1) % 5][j1] + key[(i2 + 1) % 5][j2]
        else:
            res += key[i1][j2] + key[i2][j1]
    return res

def play_fair_decrypt(encode_str, key_str):
    key = generate_key_matrix(key_str)

    def find_position(char):
        for i in range(5):
            for j in range(5):
                if char == key[i][j]:
                    return i, j

    res = ''

    for i in range(0, len(encode_str), 2):
        i1, j1 = find_position(encode_str[i])
        i2, j2 = find_position(encode_str[i + 1])
        if i1 == i2:
            res += key[i1][(j1 - 1) % 5] + key[i2][(j2 - 1) % 5]
        elif j1 == j2:
            res += key[(i1 - 1) % 5][j1] + key[(i2 - 1) % 5][j2]
        else:
            res += key[i1][j2] + key[i2][j1]
    return res


if __name__ == "__main__":
    a = play_fair_encrypt('HELLOONEAnDALL', 'KEY')
    b = play_fair_decrypt(a, 'KEY')
    print('Encode: ', a)
    print('Decode: ', b)
