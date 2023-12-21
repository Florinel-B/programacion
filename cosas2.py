def reversible(N):
    palindromo = True
    i= 0
    a = len(N)-1
    while i <= len(N)//2 and palindromo:
        if N[i] == N[a]:
            i+= 1
            a-=1
        else:
            palindromo = False

    return palindromo


print("DIME UNA PALABRA Y TE DIRE SI ES POLINDROMA")
palabra= input("dame la palabra: ")
if reversible(palabra):
    print ("es reversible ")
else:
    print("no es reversible")