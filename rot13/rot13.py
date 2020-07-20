# rot13 Encryption Algorithm

""" Given a string, rotate each letter x spaces through the alphabet """


def rot13(_encrypt, _rot_by):
    """ rot13 encryption algorithm
    :param _encrypt: message to encrypt
    :param _rot_by: rotate letters by """
    _encrypted = ""
    for letter in _encrypt:
        temp = ord(chr(ord(letter) + _rot_by))
        if temp > 122:
            enc = 96 + (temp - 122)
        elif temp < 97:
            enc = 122 - (96 - temp)
        else:
            enc = temp
        _encrypted += chr(enc)
    return _encrypted


# program driver
if __name__ == '__main__':
    msg = input('Encrypt: ')
    rot = int(input('Rotate By: '))
    encrypted = rot13(msg, rot)
    print(encrypted)
    print(rot13(encrypted, -rot))
