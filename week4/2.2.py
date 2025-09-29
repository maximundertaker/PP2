#2. Fahrenheit to Celsius
# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def f_to_c(f):
    return (5 / 9) * (f - 32)

f = int(input())
print(f"{f}°F = {f_to_c(f):.2f}°C")