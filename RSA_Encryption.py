def encrypt(plaintext,public_key):
	key,n = public_key
	cipher = [chr((ord(char) ** key) % n) for char in plaintext]
	cipher2 = [(ord(char) ** key) % n for char in plaintext]  
	return ''.join(cipher) , cipher2
