#!/usr/bin/python

# string X
# string é a string que sofrerá o ROT
# X é o valor do ROT

import sys

string = sys.argv[1]

x = int(sys.argv[2])

print("String: ", string)
print("rot" + str(x))

# ASCII to int
string2 = [ord(letter) for letter in string]
print(string2)

'''
for i in range(len(string2)):
	string2[i] = string2[i] + x
'''

# int to ASCII
string3 = [chr(letter) for letter in string2]
print(string3)
