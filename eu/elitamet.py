from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Assume 'private_key' is the RSA private key and 'message' is the data to be signed
private_key = RSA.import_key(open('private.pem').read())
message = b'This is the message to hash and sign'
hash = SHA256.new(message)

# Sign the hash with the private key
signature = pkcs1_15.new(private_key).sign(hash)
