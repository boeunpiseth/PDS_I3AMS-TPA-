#Problem 1: Student ID
name = "Visal"
age = 20
major = "AMS"
gpa = 4.0
is_scholar = True

print("=" * 30)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")
print("=" * 30)

for value in [name, age, major, gpa, is_scholar]:
    print(f"{value!r} -> {type(value).__name__}")

age = "20"
print(f"After reassignment, type(age) = {type(age).__name__}")
