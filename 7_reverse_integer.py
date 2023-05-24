# 7. Reverse Integer

def reverse(x: int) -> int:
    def repeat(y: int) -> int:
        number = y
        reverse = 0
        while number:
            reverse = reverse * 10 + number % 10
            number //= 10
        return reverse

    if x >= 0:
        result = repeat(x)
    else:
        x = x * -1
        result = -1 * repeat(x)

    if result in range(-2**31, 2**31 - 1):
        return result
    else:
        return 0


x = reverse(123)
print(x)
