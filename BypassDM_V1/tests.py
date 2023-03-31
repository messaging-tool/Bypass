from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
cc = key.decode()

print(cc)
print(type(cc))

dd = cc.encode()
print(dd)
print(type(dd))