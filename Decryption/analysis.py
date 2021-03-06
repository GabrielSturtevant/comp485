#!/usr/bin/python

# This script was used to analyze the frequency with which the letters of the encrypted message appeared. This helped me
# determine which offset was used for the caesar cipher. It takes a message and runs through all 26 permutations of the
# the caesar cipher, outputting each one to a file named analysis.txt in descending order from most commonly used letter
# to least commonly used.
#
# This script is atomic and is not used in the decryption program.


def cipher(lst, key):
	to_return = []
	ascii_lst = []
	for x in lst:
		ascii_lst.append(ord(x))
	for x in ascii_lst:
		x -= key
		if x < 65 and not x == 35:
			x += 26
		to_return.append(chr(x))
	return to_return


def analyze_letter_frequency():
	message = 'DRPWPWXHDRDKDUBKIHQVQRIKPGWOVOESWPKPVOBBDVVVDXSURWRLUEBKOLVHIHBKHLHBLNDQRFLOQ'
	to_write = open('./analysis.txt', 'w+')
	
	for x in range(1, 27):
		message_list = list(message)
		library = refresh()
		message_list = cipher(message_list, x % 26)
		for y in message_list:
			library['{}'.format(y)] += 1
		to_write.write('Key : {}\n-------------\n'.format(x))
		string_lst = []
		for y in range(65, 91):
			string_lst.append([chr(y), library[chr(y)]])
		string_lst = sorted(string_lst, key=lambda frequency: frequency[1], reverse=True)
		for z in string_lst:
			var = "{0} : {1}\n".format(z[0], z[1])
			to_write.write(var)
		to_write.write('\n')
		

def refresh():
	library = {}
	for x in range(ord('A'), ord('Z')+1):
		library['{}'.format(chr(x))] = 0
	return library

analyze_letter_frequency()
