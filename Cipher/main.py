from decryption_object import *
import sys

message = 'DRPWPWXHDRDKDUBKIHQVQRIKPGWOVOESWPKPVOBBDVVVDXSURWRLUEBKOLVHIHBKHLHBLNDQRFLOQ'
foo = decryption_obejct(message)
foo.open_file()
for i in range(26):
    for j in range(2,10):
        foo.setup_matrix(foo.return_ascii_ciphered_list(i), j)
        sys.stdout.write("New Caesar Key\n")
