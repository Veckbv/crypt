s = 'GRIREAAEEALRALSNNLLITFT EWAVHPT '


def decrypt_skital(m, crypt_s):
    decrypt_s = ''
    n = (len(crypt_s) - 1) // m + 1
    for i in range(m):
        s = 0
        for j in range(n):
            if i + s > len(crypt_s) - 1:
                continue
            decrypt_s += crypt_s[i + s]
            s += m     
    return decrypt_s


for i in range(1, len(s)):
    print(f"{i} {decrypt_skital(i, s)}")