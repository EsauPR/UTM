#!/bin/bash

if [[ $1 ]]; then

	stty 9600 -F /dev/ttyUSB0 dec cread cs8

	first=true

	for line in $(cat $1); do
		if [[ $first == false && ${line:1:2} != "00" ]]; then
			
				hex="\x00\x${line:1:2}\x${line:3:2}\x${line:5:2}"
				line=${line:9}

				for (( i = 0; i < $((${#line}-2)); i=i+2 )); do
					hex="$hex\x${line:$i:2}";
				done

				echo "Enviando: $hex"
				
				echo -e $hex > sal
				cat sal > /dev/ttyUSB0
		fi
		first=false
	done

	
	echo -e "\x01" > sal
	cat sal > /dev/ttyUSB0
	rm sal

else
	echo "Error: missing file input"
	exit
fi
