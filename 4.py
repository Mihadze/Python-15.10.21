a=int(input("сартовое количество: "))
b=int(input("среднесуточое увеичение, в процентах: "))
c=int(input("количество дней для размножения: "))
d = 1 + b/100
print("день           популяция")
for i in range (1, c+1):
    a = a*d
    print(i , "            ", a )
