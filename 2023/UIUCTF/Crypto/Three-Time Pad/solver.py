import binascii

def xor(s1,s2):
	key = bytes([a ^ b for a, b in zip(s1,s2)])
	return key

if __name__=="__main__":
	c1 = "14f5f95b4a252948a8aef177d6c92d82e3016362bd7463f41f40a00ad9e0ccad911b959ef8dfad5f1cc4481ecb64"
	c2 = "06e2f65a4c256d0ba8ada164cecd329cae436069f83476e91757e91bd4a4cce2c60a8f9aac8cb14210d55253cd787c0f6a"
	c3 = "03f9ea574c267249b2b1ef5d91cd3c99904a3f75873871e94157df0fcbb5d1eab94f9386"
	p2 = "printed on flammable material so that spies could"
	
	c1 = binascii.unhexlify(c1)
	c2 = binascii.unhexlify(c2)
	c3 = binascii.unhexlify(c3)
	p2 = p2.encode('utf-8')
	
	# Obtain the key of c2 by XOR-ing c2 with p2
	key = xor(c2,p2)
	print("Key value: ", key)
	
	# Try to decrypt c1 and c3 using the key
	p1 = xor(c1,key)
	p3 = xor(c3,key)
	
	p1 = p1.decode('utf-8')
	p3 = p3.decode('utf-8')
	print("Decrypted p1: ", p1)
	print("Decrypted p3: ", p3)

