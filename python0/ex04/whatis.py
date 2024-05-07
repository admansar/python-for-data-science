import sys

def odd (n):
	if n % 2 :
		print ("I'm Odd.");
	else:
		print ("I'm Even.");

if len (sys.argv) == 2:
	try:
		odd (int(sys.argv[1]));
	except:
		print ("AssertionError: argument is not an integer");
else :
	print ("AssertionError: more than one argument is provided");
