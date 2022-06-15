# WAP to find whether a container with a L and another with b L capacity can measure m L milk or not.
'''
Input : a=2L, b=5L and m=4L
'''


def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def check_can_measure(a, b, m):
    if a==m or b==m or a+b ==m or a-b ==m or b-a == m:
        return True
    elif a+b <m:
        return False
    else:
        hcf = gcd(a,b) 
        if hcf == 1:
            return True
        elif m%hcf == 0:
            return True
        else: 
            return False

print(check_can_measure(3,5,4))
