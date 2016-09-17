from decryption_object import *
from word_organizer import organize_results
import sys

message = 'DRPWPWXHDRDKDUBKIHQVQRIKPGWOVOESWPKPVOBBDVVVDXSURWRLUEBKOLVHIHBKHLHBLNDQRFLOQ'
foo = decryption_obejct(message)
foo.open_file()
for i in range(26):
    #for j in range(2,7):
    foo.setup_matrix(foo.return_ascii_ciphered_list(i), 7, i)
    sys.stdout.write("New Caesar Key\n")

organize_results("results.txt", "results.txt")
