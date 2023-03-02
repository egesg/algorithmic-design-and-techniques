# number theory, cryptography

def naive_gcd(a, b):
    best = 0
    for d in range(1, a+b):
        if a%d == 0 and b%d == 0:
            best = d
        d += 1
    return best

print(naive_gcd(3918848,1653264))
# 61232
