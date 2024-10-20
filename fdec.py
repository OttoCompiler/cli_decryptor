
"""

simple CLI decryptor

"""

import sys
from Crypto.Cipher import AES
import base64


BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
    BLOCK_SIZE - len(s) % BLOCK_SIZE
)
unpad = lambda s: s[: -ord(s[len(s) - 1:])]


def _r(fpath: str):
    return open(fpath).read()


def _rb(fpath: str):
    return open(fpath, 'rb').read()


def decrypt_str(enc, password):
    private_key = password.encode("utf-8")
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return unpad(cipher.decrypt(enc[16:]))


if __name__ == '__main__':
    print()
    try:
        fpath = sys.argv[1]
        ekey = sys.argv[2]
        fc = _rb(fpath)

        try:
            dec = decrypt_str(fc, ekey)
        except Exception as e:
            print(e)
            sys.exit(1)
        dec = base64.b64decode(dec).decode()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()
        print(dec)
        print()
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    except:
        print('error: no file path provided')
        print()

