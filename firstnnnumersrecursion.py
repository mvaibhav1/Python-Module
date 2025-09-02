def natural_numbers_sum(n):
    if(n==0):
        return n
    return n + natural_numbers_sum(n-1)

n=int(input("enter the number : "))

#function Calling     
print(natural_numbers_sum(n))