alph = [chr(ord('a') + i) for i in range(26)]
s = 'vbqwyivxgshofjeiycfbu'

def decrypt_cesar(k, crypt_s):
    decrypt_s_shift_right = [alph[(alph.index(c) + k) % 26] for c in crypt_s]
    decrypt_s_shift_left = [alph[(alph.index(c) - k) % 26] for c in crypt_s]
    return ''.join(decrypt_s_shift_left), ''.join(decrypt_s_shift_right)

print(decrypt_cesar(16, s))