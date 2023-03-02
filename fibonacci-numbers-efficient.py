def fib_list(n):
    f_list = [0, 1] # f[0] = 0, f[1] = 1 -> base cases

    for i in range(2, n+1):
        f_list.append(f_list[i-1] + f_list[i-2])
    return f_list[n]

print(fib_list(10))
# 55

# O(n^2)