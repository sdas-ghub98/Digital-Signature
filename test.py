import RSA_Encryption
import RSA_Decryption
import hashlib
import key_generation

def main():

	#Take the plaintext and hash it using SHA-224
	m = input('Enter plain text : ')
	h1 = hashlib.sha224(m.encode())
	print ('Applying SHA224 on plain text : ' + h1.hexdigest() + '\n')
	
	#Generate the keys from key_generation
	pu,pr = key_generation.generate_key()
	
	#Encrypt the output using RSA
	ct , a = RSA_Encryption.encrypt(h1.hexdigest(),pu)
	print('The cipher text is : ',ct)
	
	#Decrypt the output using RSA
	pt = RSA_Decryption.decrypt(a,pr)
	print('The plaintext decrypted is : ',pt)
		
	#Hash it again
	#h2 = hashlib.sha224(pt.encode())
	#print ('SHA224 on the decrpyted text : ' + h2.hexdigest() + '\n')
	
	#Compare the hash value generated with the first hash value
	#if (h1 == h2):
	 #       print('The digital signature has been verified!!')
	#else:
	 #       print('Sorry, the digital signature could not be verified...')

if __name__ == '__main__':
	main()
