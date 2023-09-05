from random import randint
def list_change (mi, ma, list):
    list_res = []
    for i in range (0, len(list)):
        if mi < list[i] < ma:
            list_res.append(i)
    return list_res
        
n = int(input("Enter numbers of items: "))
initial_list  = [randint(1,100) for i in range(n)]
print(initial_list)
mn = int(input("Enter minimum: "))
mx = int(input("Enter maximum: "))

print(list_change(mn, mx, initial_list))