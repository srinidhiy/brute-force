from itertools import product
import string
import hashlib
import time
###read in the file###
with open("passwords.txt", "r") as file:
    pass_list = [x.strip() for x in file]
#    print(pass_list)
file.close()

###loop 1-8 so that repeat = the current number###
time0 = time.time()
result = string.printable
for i in range (1,9):
###iterate through every combination (product function)###
    for j in product(result, repeat=i):
        ###hash each combination###
        hash_ = ''.join(j)
        hashed_attempt = hashlib.md5(hash_.encode())
#        print(hashed_attempt.hexdigest())
        ###iterate through the list that holds all the hashes, see if there is a match###
        for k in range(len(pass_list)):
            if hashed_attempt.hexdigest() == pass_list[k]:
                time1 = time.time()
                time_diff = time1 - time0
                print("Password found: " + hash_ + "\t Time: " + str(time_diff))
                break
            else:
                continue
                


