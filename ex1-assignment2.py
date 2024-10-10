list1 = [54, 76, 2, 4, 98, 100]

int1 = int(input("Input the first integer: "))
int2 = int(input("Input the second integer: "))
lower= min(int1,int2)
upper= max(int1,int2)
print(f"the number between  {lower},{upper} is:")
for num in list1:
    if lower<=num <= upper:
        print(num)