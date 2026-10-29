#problem 7: Digit Tools <a,b>
def digit_sum(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_value = 0
    while n > 0:
        reversed_value = reversed_value * 10 + n % 10
        n //= 10
    return sign * reversed_value


def is_palindrome(n):
    return n >= 0 and n == reverse_number(n)


for number in (2026, 12321, 9875):
    print(
        f"{number}: digit sum = {digit_sum(number)}, "
        f"reversed = {reverse_number(number)}, palindrome = {is_palindrome(number)}"
    )
palindrome_count = sum(1 for number in range(10, 1000) if is_palindrome(number))
print(f"Palindromes from 10 to 999: {palindrome_count}")