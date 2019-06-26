import base64 as b64


def add_encrypt(tips, key):
    lkey = len(key)
    secret = []
    num = 0
    for each in tips:
        if num >= lkey:
            num = num % lkey
        secret.append(chr(ord(each) + ord(key[num])))
        num += 1
    #return b64.b64encode( "".join( secret ).encode() ).decode()
    return "".join(secret)


def sub_decrypt(secret,key):
    #tips = b64.b64decode( secret.encode() ).decode()
    tips = secret
    lkey = len(key)
    secret = []
    num = 0
    for each in tips:
        if num >= lkey:
            num = num % lkey
        secret.append(chr(ord(each) - ord(key[num])))
        num += 1
    return "".join(secret)


tips = "jdahfjohohihwoifhohfhefiow"
key = "hohoho"
secret = add_encrypt(tips, key)
print("cipher_text:", secret)
plaintxt = sub_decrypt(secret, key)
print("plain_text:", plaintxt)
