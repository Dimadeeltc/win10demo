def power_sum(power, *args):
    total = []
    for i in args:
        total.append(pow(i, power))
    return total

s = power_sum(3, 1, 2, 5)
print(s)
