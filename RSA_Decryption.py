def decrypt(ciphertext, private_key):
	key,n = private_key
	ciphertext = str(ciphertext)
	plain = [chr((char ** key) % n) for char in ciphertext]
	return ''.join(plain)
