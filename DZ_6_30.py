def progression (a,b,c):
    list_res = []
    for i in range (0, b):
        list_res.append(a)
        a = a +c
    return list_res
        

a1 = int(input("Enter initial term of progression: "))
n = int(input("Enter numbers of terms: "))
d = int(input("Enter common difference: "))

print(*progression(a1, n, d))

