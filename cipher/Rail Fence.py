def encrypt_rail_fence(text, key):
    rail = [['/n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key-1):
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else :
            row -= 1
    
    res = ''
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '/n':
                res += rail[i][j]

    return res

def decrypt_rail_fence(cipher, key):
    rail = [['/n' for i in range(len(cipher))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(cipher)):
        if (row == 0) or (row == key-1):
            dir_down = not dir_down
        
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else :
            row -= 1
    
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*':
                rail[i][j] = cipher[index]
                index += 1

    dir_down = False
    row, col = 0, 0
    res = ''

    for i in range(len(cipher)):
        if (row == 0) or (row == key-1):
            dir_down = not dir_down
        
        res += rail[row][col]
        col += 1

        if dir_down:
            row += 1
        else :
            row -= 1

    return res

encode = encrypt_rail_fence('GeeksforGeeks', 3)
decode = decrypt_rail_fence(encode, 3)
print(encode)
print(decode)