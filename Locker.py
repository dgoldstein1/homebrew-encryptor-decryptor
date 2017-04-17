"""Created by David Goldstein on 6/4/2016

Encrypts using keys generated from user specified password.
Decryption is done from same password.

"""

import sys
import time
from datetime import *

def random(length):
	"""generates random number in range 0 - 1 with length 20"""
	seed = datetime.now().microsecond # 6 digit seed
	num = middleSquares(seed,length)
	return float("0." + num)

def randomList(length,nDigits,low,high):
	"""creates random list of numbers between low and
	high with a length nDigits.  List has length 'length'"""
	listRan = [None] * length
	i = 0
	while(i<length):
		listRan[i] = (random(nDigits) * (high-low)) + low
		i += 1
	return listRan

def randomSeededList(length,nDigits,low,high,initSeed):
	"""creates random list of numbers with specified parameters
	starts with user specified initial seed for easy decryption """
	if length < 1 or nDigits < 1 or initSeed == 0:
		print "Invalid inputs for randomSeededList()"
		exit(1)
	toReturn = [None] * length
	n = str(middleSquares(nDigits * length,initSeed))

	for i in range(0,length):
		ranN = float("0." + n[i * nDigits : (i * nDigits) + nDigits])
		toReturn[i] = (ranN * (high-low)) + low
	return toReturn


def middleSquares(nDigits,seed=None):
	"""recursion method of Middle Squares. returns semi random num
	nDigits is desired length """
	if seed == None:
		seed = datetime.now().microsecond # 6 digit seed

	randomN = 0
	for i in range(0,(nDigits / 3) + 1):
		seed = getMiddleDigits(seed * seed)
		randomN = (randomN * 1000) + seed

	#truncate to desired length
	while(randomN / (10 ** nDigits) > 1):
		randomN /= 10

	return randomN
	

def getMiddleDigits(n):
	"""returns three middle digits of any number"""
	if(n<=99 and n >=-99):
		return n * 100
	n = str(abs(n))
	return int(n[(len(n) / 2) -1] + n[len(n) / 2] + n[(len(n) / 2) + 1])



class BitwiseOneTimePad:

	def encrypt(self,plainStr,password):
		"""shifts characters a random amount each time
		keys are specified by user"""
		initialSeed = 1
		i = 0
		for char in password:
			if i <= 10 and ord(char) != 0:
				initialSeed *= ord(char)
				i += 1
			initialSeed += ord(char)

		keys = randomSeededList(3,2,0,100,initialSeed) #between 0 and 100 with 3 digit precision, len of message

		keyLen = len(keys)
		stringOut = ""
		i = 0
		for char in plainStr:
			stringOut += chr(ord(char) ^ int(keys[i]))
			i = (i + 1) % keyLen #cycles through keys
		return stringOut

	def decrypt(self,encryptedStr,password):
		"""decryption of message shift based on XOR
		keys are created using user password"""
		return self.encrypt(encryptedStr,password) #XOR encrypt = decrypt
		
if __name__ == "__main__": #run from console

	if(len(sys.argv) != 4):
		print  "Usage: python Locker.py encrypt/decrypt $file $password"
	else:
		msg = open(sys.argv[2], 'r').read()
		password = str(sys.argv[3])
		eFile =  open(sys.argv[2],'rb+')

		if sys.argv[1] == "encrypt":
			encryptedMsg = BitwiseOneTimePad().encrypt(msg,password)
			eFile.seek(0)
			eFile.truncate()
			eFile.write(encryptedMsg)
			
		if sys.argv[1] == "decrypt":
			decryptedMsg = BitwiseOneTimePad().decrypt(msg,password)
			eFile.seek(0)
			eFile.truncate()
			eFile.write(decryptedMsg)
