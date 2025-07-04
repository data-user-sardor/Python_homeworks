# 1 - task is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, 
# aks holda False qiymat qaytarsin.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4)) 
print(is_prime(7))

# 2 - task digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi 
def digit_sum(k):
    total = 0
    while k > 0:
        total += k % 10
        k //= 10
    return total

print(digit_sum(24))   
print(digit_sum(502))

# 3 - task Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini 
# (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def print_powers_of_two(n):
    power = 1
    while (power := power * 2) <= n:
        print(power, end=' ')

print_powers_of_two(10)
