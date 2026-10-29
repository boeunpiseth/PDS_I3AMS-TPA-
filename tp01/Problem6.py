#problem 6: leap year and days in month <a,b,c,d>
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    if month < 1 or month > 12:
        return None
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


for year in (1900, 2000, 2024, 2026):
    print(f"{year} {'leap' if is_leap(year) else 'not leap'}")

print(
    f"Feb 2024: {days_in_month(2, 2024)} | "
    f"Feb 2026: {days_in_month(2, 2026)} | "
    f"Apr: {days_in_month(4, 2026)} | month 13: {days_in_month(13, 2026)}"
)
leap_count = sum(1 for year in range(2000, 2101) if is_leap(year))
print(f"Leap years from 2000 to 2100: {leap_count}")
