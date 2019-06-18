#Дешифр цезаря
alph = [chr(ord('a') + i) for i in range(26)]
s = 'vbqwyivxgshofjeiycfbu'

def decrypt_cesar(k, crypt_s):
    decrypt_s_shift_right = [alph[(alph.index(c) + k) % 26] for c in crypt_s]
    decrypt_s_shift_left = [alph[(alph.index(c) - k) % 26] for c in crypt_s]
    return ''.join(decrypt_s_shift_left), ''.join(decrypt_s_shift_right)

# print(decrypt_cesar(16, s))


#Дешиф Скитала(Древней Спарты)
s2 = 'GRIREAAEEALRALSNNLLITFT EWAVHPT '

def decrypt_skital(m, crypt_s):
    # split_crypt_s = ''
    decrypt_s = ''
    n = (len(crypt_s) - 1) // m + 1
    # print(n)
    # for i in range(1, len(s) + 1):
    #     split_crypt_s += s[i-1]
    #     if i % m == 0:
    #         split_crypt_s += ' '
    for i in range(m):
        s = 0
        for j in range(n):
            if i + s > len(crypt_s) - 1:
                continue
            decrypt_s += crypt_s[i + s]
            s += m
            # print(f'{i} {j} {s} {decrypt_s}')
            
    return decrypt_s


for i in range(1, len(s2)):
    print(f"{i} {decrypt_skital(i, s2)}")
    
