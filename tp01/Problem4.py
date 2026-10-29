#Problem 4: Type Conversion <Part a,b,c>
print("int('7') + 3.5 =", int("7") + 3.5)
print("str(10) * 3 =", str(10) * 3)
print("bool(''), bool(' ') =", bool(""), bool(" "))
print("int(3.99) =", int(3.99))
print("float('1e3') =", float("1e3"))
print("int(True) + float('2.5') =", int(True) + float("2.5"))
print("round(2.5), round(3.5) =", round(2.5), round(3.5))
print("type(10 / 2) =", type(10 / 2).__name__)


def safe_int(text):
    try:
        return int(float(text.strip()))
    except (ValueError, AttributeError, OverflowError):
        return None


for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))

first = safe_int(input("Enter the first number: "))
second = safe_int(input("Enter the second number: "))
if first is None or second is None:
    print("Please enter valid numbers.")
else:
    print("Sum:", first + second)
