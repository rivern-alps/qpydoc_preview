import uhashlib
import ubinascii
# 目前支持 md5，sha1, sha256

data = b"QuecPython"  # 待加密数据

hash_obj = uhashlib.md5()
hash_obj.update(data)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("md5加密后的数据：", hex_msg)
# b'37b8419ee7cdb3c64d7e66019216117c'

hash_obj = uhashlib.sha1()
hash_obj.update(data)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("sha1加密后的数据：", hex_msg)
# b'614a4247ef68e9f9793e11353cc86acb932badab'

hash_obj = uhashlib.sha256()
hash_obj.update(data)
res = hash_obj.digest()
hex_msg = ubinascii.hexlify(res)
print("sha256加密后的数据：", hex_msg)
# b'1ec66771b3a9ac3ea4c44f009e545797d42e9e7d426fff8275895468fe27c6cd'


# print("原始数据：", b'\x11\x22\x33123')
# res = ubinascii.b2a_base64('\x11\x22\x33123')
# print("编码base64数据：", res)
# res = ubinascii.a2b_base64(res)
# print("还原base64数据：", res)
