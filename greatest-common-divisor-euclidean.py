# a' : the remainder when a is devided by b
# gcd(a, b) = gcd(a', b) = gcd(b', a)

# because
# a = a' + bq for some q
# d divides a and b if and only if it devides a' and b


def euclid_gcd(a, b):
    if b == 0:
        return a
    
    return euclid_gcd(b, a % b)

print(euclid_gcd(3918848,1653264))
# 61232

