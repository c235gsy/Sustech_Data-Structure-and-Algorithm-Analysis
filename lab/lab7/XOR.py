import base64 as b64


def xor_encrypt(tips,key):
    lkey = len(key)
    secret = []
    num = 0
    for each in tips:
        if num >= lkey:
            num = num % lkey
        secret.append(chr(ord(each) ^ ord(key[num])))
        num += 1

    #return b64.b64encode( "".join( secret ).encode() ).decode()
    return "".join(secret)


def xor_decrypt(secret,key):
    #tips = b64.b64decode( secret.encode() ).decode()
    tips = secret
    lkey = len(key)
    secret = []
    num = 0
    for each in tips:
        if num >= lkey:
            num = num % lkey
        secret.append(chr(ord(each) ^ ord(key[num])))
        num += 1
    return "".join(secret)


tips= "1234567"
key= "well"
secret = xor_encrypt(tips,key)
print( "cipher_text:", secret )
plaintxt = xor_decrypt( secret, key )
print( "plain_text:",plaintxt )
