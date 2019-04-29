import random
import cryptomath

def isPrime(num):
	if(num == 2):
		return True
	elif(num == 0 or num == 1 or num%2 == 0):
		return False
	else:
		for i in range(3,num):
			if(num%i == 0):
				return False
			if(i*i == num):
				return False
	return True
			
	
def generate_key():
	keySize = 8
	primes = [i for i in range(0,500) if isPrime(i)]
	p = random.choice(primes)
	q = random.choice(primes)
	n = p*q
	phi_n = (p-1)*(q-1)
	while True:
		e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
		if (cryptomath.gcd(e,phi_n)==1):
			break
	d = cryptomath.findModInverse(e,phi_n)
	public_key = (n,e)
	private_key = (n,d)
	print ('FOR CURRENT RUN: \n', 'Public key : ',public_key,'\t Private key : ',private_key)
	return (public_key,private_key)
