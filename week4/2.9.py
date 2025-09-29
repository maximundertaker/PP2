#9. Sphere Volume
# Write a function that computes the volume of a sphere given its radius.

def sphere(radius):
    return (4/3) * 3.14 * radius ** 3
r = int(input())
print(f"Volume: {sphere(r):.2f}")