# Homebrew Encryptor / Decryptor

A basic encryptor / decryptor class in python, made from scratch. Obviously, use a professional library for any professional encryption.

## Structure

There are two classes: 
	-Random seed generator
	-One Time pad

The random seed generator generates a pseudo-random sequence based on the user-specified key. The Bitwise one time pad takes this sequences and XORs every byte in the given file, and writes the output to the file.


## Test

```sh
./test.sh
```
If run successfully should return ```SUCCESS``` and create ```tests/``` directory.

## Run


```sh
python Locker.py encrypt/decrypt $file $password
```

### Example



```sh
touch example.txt
echo "To thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man." >> example.txt 

python Locker.py encrypt example.txt samplePassword
cat example.txt

python Locker.py decrypt example.txt samplePassword
cat example.txt

```

After Encryption:
v?q[%|$n\kjW')|?kG.5*wVkpFktG8m-v^'vEg9S89F#|%pU#m?qWk}S25?q]>9Q*wA?9\$m?qW%9P.9T*uA.9F$9S%`&x\e

After Decryption:
To thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man.

## Authors

* **David Goldstein** - [DavidCharlesGoldstein.com](http://www.davidcharlesgoldstein.com/?github-homebrew-encyptor) - [Decipher Technology Studios](http://deciphernow.com/)

