'''
A number is called happy if it leads to 1 after a sequence of steps
wherein each step number is replaced by the sum of squares of its digit that
is if we start with Happy Number and keep replacing it with digits square sum,
we reach 1.
Input: n = 19
Output: True
19 is Happy Number,
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
As we reached to 1, 19 is a Happy Number.
Input: n = 20
Output: False
'''
#create happy number function-->
def isHappyNum(num):
    rem = s = 0

    #logic to as squares os number--->
    while(num > 0):
        rem = num % 10
        s = s + (rem * rem)
        num = num // 10
        return s
#main
num = int(input("Enter an number : "))
result = num

while(result != 1 and result != 4):
    result = isHappyNum(result)

#Happy number always ends with 1---->
if(result == 1):
    print("number is Happy number")
    print("True")
#Not happy no is ends with 4---->
elif(result == 4):
    print("number is not Happy")
    print("False")
    
