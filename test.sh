#tests individual file enccryption / decryption


mkdir tests
if [ $? -eq 0 ]; 
then
	rm -r tests
	mkdir tests
fi

sourceFile="tests/example.txt"
destinationFile="tests/destination.txt"
password="password"
username="dave"

touch $sourceFile
touch $destinationFile

> $sourceFile
> $destinationFile

echo "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." >> $sourceFile

cp $sourceFile $destinationFile


#encrypt and decrypt
python Locker.py encrypt $sourceFile samplePassword
python Locker.py decrypt $sourceFile samplePassword

#test input / output
if cmp -s $sourceFile $destinationFile
then 
   echo "SUCCESS"
else
   echo "FAILURE: see files for details"
   exit
fi
