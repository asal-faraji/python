num = 99
while num >= 10:
    is_prime = True  # فرض می‌کنیم عدد اول است
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False  # اگر بر عددی بخش‌پذیر بود، اول نیست
            break
        i = i + 1
    if is_prime:
        print("بزرگترین عدد اول دو رقمی:", num)
        break
    num = num - 1

