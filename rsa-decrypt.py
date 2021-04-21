from modules.primefactors import prime_factors
from modules.modinv import modinv

# enter ciphertext here
ciphertext = "18809 06379 20209 14259 01612 10794 17580 00743 05133 09868 18458 17553 14160 15681 17168 13289 13336 10682 16512 10245 05950 03438 01949 02745 12036 07414 14107 16122 02049 07881 03844 02942 13609 07243 07347 10663 13558 04683 00383 15879 18809 05324 00922 19572 13696 02016 12815 06862 05133 08216 03844 14602 18958 13684 12214 05937 20671 07796 11609 12276 11349 07459 19229 20134 19853 18019 12535 00856 16102 19276 01052 15189 02210 00970 17859 02677 17944 14661 18160 03650 01014 09682 04643 05109 13761 10794 14107 04268 15227 11484 03844 05912 16780 15832 08364 10794 14107 05333 03384 13005 11857 21069 16361 12632 02688 03128 16187 08872 19654 12297 13634 19754 08238 06964 13864 10126 11275 14687 17915 09868 18458 12752 11551 18693 00186 00751 17580 17343 12029 08336 13634 17553 17919 10630 13839 20399 16527 05908 09763 03094 08473 01111 17919 15877 12780 04665 12535 05497 11007 05697 20974 16764 19229 17295 15458 02081 12385 14586 15227 05106 11857 07868 13606 18790 19853 19258 14107 16122 13367 16580 01969 14071 08238 13502 03755 15735 12815 16196 16512 20921 11021 09459 19229 10290 15937 02717 12483 07722 19782 19814 11867 18707 13609 07153 12036 05093 12385 00856 15880 15216 20974 02942 08828 14974 19801 19258 18403 19422 02049 20921 20974 02942 07441 20772 13985 19304 12497 05497 09307 11511 11656 17817 09475 19560 08364 15462 04550 02507 16102 17069 11400 05975 02285 14974 02292 15092 18259 12292 09345 16580 08989 12600 02746 17295 19584 06545 12535 08872 09945 10197 14058 00199 10209 03601 13166 02016 11275 03801 02356 20921 20974 20678"

ciphertext_arr = ciphertext.split()

# enter public key here
e = 13
N = 21079

# factorization
primes = prime_factors(N)
p = primes[0]
q = primes[1]

print("p = {}\nq = {}".format(p,q))

x = (p-1)*(q-1)

# calculate modular multiplicative inverse
d = modinv(e, x)
print("d = {}\n".format(d))

decrypted_numerical = []

# decrypt RSA
for block in ciphertext_arr:
    decrypted_numerical.append(pow(int(block), d, N))

decrypted_numerical_str = [str(x) for x in decrypted_numerical]

# descuffinator
for i in range(len(decrypted_numerical_str)):
    decrypted_numerical_str[i] = decrypted_numerical_str[i][:-1]
    if len(decrypted_numerical_str[i]) != 3:
        decrypted_numerical_str[i] = (3-len(decrypted_numerical_str[i])) * "0" + decrypted_numerical_str[i][:]

decrypted_joined = "".join(decrypted_numerical_str)

count = 0
x = ""
decrypted_numerical_str.clear()
for i in range(len(decrypted_joined)):
    count = count + 1
    x = x + str(decrypted_joined[i])
    if count == 2:
        decrypted_numerical_str.append(x)
        x = ""
        count = 0

# convert decimal to ascii

plaintext = ""
for letter in decrypted_numerical_str:
    plaintext = plaintext + chr(int(letter))

print(plaintext)
