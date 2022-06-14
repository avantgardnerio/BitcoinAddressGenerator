import ecdsa
from mnemonic import Mnemonic

# Step1: Generate ECDSA Private Key
mnemon = Mnemonic('english')
ecdsaPrivateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
hex = ecdsaPrivateKey.to_string().hex()
mnemonic = mnemon.to_mnemonic(bytes.fromhex(hex))
print("ECDSA Private Key: ", hex)
print("mnemonic: ", mnemonic)
print("------------------------------------------------------")
