#Problem 3: Temperature Conversion <a,b,c,d>
def celsius_to_fahrenheit(c, round_to=1):
    return round(c * 9 / 5 + 32, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    return round((f - 32) * 5 / 9, round_to)


print("  °C |    °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6.1f}")

print(f"98.6 °F = {fahrenheit_to_celsius(98.6):.1f} °C")
f = celsius_to_fahrenheit(37)
back_to_celsius = fahrenheit_to_celsius(f)
print(f"37 °C -> {f:.1f} °F -> {back_to_celsius:.1f} °C")
print(f"37 °C to Fahrenheit (3 decimals): {celsius_to_fahrenheit(37, round_to=3)}")