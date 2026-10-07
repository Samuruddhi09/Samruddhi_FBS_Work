# 3. Convert distant given in feet and inches into meter and centimeter.

# 1 foot = 12 inches
# 1 inch = 2.54 centimeters
# 1 meter = 100 centimeters

feet = float(input("Enter feet: "))
inch = float(input("Enter inches: "))

total_inches = (feet * 12) + inch

centimeter = total_inches * 2.54

meter = centimeter / 100

print("Distance in meters =", meter)
print("Distance in centimeters =", centimeter)


# Enter feet: 5
# Enter inches: 4
# Distance in meters = 1.6256
# Distance in centimeters = 162.56