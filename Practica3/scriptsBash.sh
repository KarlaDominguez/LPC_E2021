function blabla(){

	if [ $1 -ge 0 -a $1 -lt 5 ]; 
   	then
    	echo 'cumple con las especificasiones '
    
    else
    	echo 'No cumple con las especificasiones '
		return 0
  	fi
}
echo 'Da un numero entre el 0 y el 5'
read A
blabla $A
echo ' '
x=4
while [ $x -gt 1 ]

do
   x=$(($x - 1 ))
   echo '    '$x	   
done
echo '   bye'