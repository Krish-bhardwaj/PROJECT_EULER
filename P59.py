def decrypt(array, key):
    en = []
    j = 0
    for i in range(len(array)):
        en.append(chr(array[i] ^ int(ord(key[j]))))
        j += 1
        if j > 2:
            j = 0
    en = ''.join(en)

    return en


def to_ascii(text):
    return [ord(c) for c in text]


def main():
    # read the crypted text
    f = open('cipher.txt')
    cipher = f.read().strip().split(',')
    f.close()

    # convert to int
    cipher = [int(x) for x in cipher]

    # cut in 3 parts
    c = []
    for i in range(3):
        c.append(cipher[i::3])

    # find the most used char in each / it should be ' '
    key = []

    for i in range(3):
        dic = {}
        for ch in c[i]:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        # reverse the dic
        dic = {dic[k]: k for k in dic}
        crypted = max(dic.items())[1]

        # reverse the xor to get the key that makes the number = ' '
        key.append(chr(crypted ^ ord(' ')))

    key = ''.join(key)

    # decrypt / convert and sum
    return sum(to_ascii(decrypt(cipher, key)))
print(main())