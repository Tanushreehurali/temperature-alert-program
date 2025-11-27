import sys


if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = float(sys.argv[1])
    print("User provided input temperature:")
else:
    script_name = sys.argv[0]
    temp = 25.0  
    print("No input given — using default temperature:")


if temp < 15:
    status = "Cold"
elif 15 <= temp <= 30:
    status = "Normal"
else:
    status = "Hot"


print("Script Name:", script_name)
print("Temperature (°C):", temp)
print("Status:", status)
