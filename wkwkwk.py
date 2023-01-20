def ditambah (P, Q):
    return P + Q
def dikurangi (P, Q):
    return P - Q
def dikali (P, Q):
    return P * Q
def dibagi (P, Q):
    return P / Q

print ("Mau diapain angkanya.")
print ("a. Ditambah")
print ("b. Dikurangi")
print ("c. Dikali")
print ("d. Dibagi")

choise = input("Input Pilihanmu (a/ b/ c/ d)")

num_1 = int (input("Input angka pertama :"))
num_2 = int (input("Input angka kedua :"))

if choise == 'a':
    print (num_1, "+", num_2, '=', ditambah(num_1, num_2))
elif choise == 'b':
    print (num_1, "-", num_2, '=', dikurangi(num_1, num_2))
elif choise == 'c':
    print (num_1, "*", num_2, '=', dikali(num_1, num_2))
elif choise == "d":
    print (num_1, "/", num_2, '=', dibagi(num_1, num_2))
else :
    print ("kayanya salah ketik, baca yang bener")