cp day5.txt day5sed.txt
sed -i ":a; $(for a in q w e r t y u i o p a s d f g h j k l z x c v b n m ; do echo s/$a${a^^}//g ; echo s/${a^^}$a//g ; done); ta" day5sed.txt

wc day5sed.txt
echo "subtract 1"
