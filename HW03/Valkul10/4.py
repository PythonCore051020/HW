num = int(input("Enter number: "))
a = num % 10
b = (num % 100) // 10
c = (num % 1000) // 100
d = num // 1000
res =a*b*c*d
print("Product:",res)
num1 = d,c,b,a
n_list = list(num1)
n_list.reverse()
print("Reverse:",n_list)
n_list.sort()
print("Sort:",n_list)