from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
print(key)
cc = key.decode()

print(cc)
print(type(cc))

dd = cc.encode()
print(dd)
print(type(dd))

print(dd==key)
ee = Fernet(dd)

print("\n\n\n\n")
encrypted_data = f.encrypt(b"This message is being encrypted and cannot be seen!")
print("\n\n------------------")
print(type(encrypted_data))
print(encrypted_data)
dec = ee.decrypt(encrypted_data)
print(dec)

