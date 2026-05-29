def tub_yoki_tub_emas(son):
    if son < 2:
        return False
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            return False
    return True

print(tub_yoki_tub_emas(25))  # True
print(tub_yoki_tub_emas(30))  # False
