def decrypt(ciphertext, private_key):
	n, key = private_key
	ciphertext = str(ciphertext)
	plain = [chr((ord(char) ** key) % n) for char in ciphertext]
	return ''.join(plain)
