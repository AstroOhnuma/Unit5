#Astro Ohnuma
#11/30/17
#warmup15.py - taking a list as an argument and returns another list where each number is doubled

def doubled(A):
    double = []
    for i in A:
        double.append(i*2)
    return double
print(doubled([2,4,6]))