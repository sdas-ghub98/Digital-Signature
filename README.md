# Digital Signature

This is a simple implementation of Digital Signature using SHA and RSA algorithm. The procedure goes like this:

1. A user enters a plain text.
2. It gets hashed using SHA-224.
3. The hash gets encrypted using RSA Algorithm and public key
4. The encrypted message is decrypted back using private key of user
5. The plain text is again using the same hash function used.
6. The end results are compared. If they join, they are verified. Otherwise they are not legitimate.
