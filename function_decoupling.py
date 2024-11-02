feet_inch = input ("Enter feet and inches: ")

def parse(feet_inch):
    parts = feet_inch.split(" ")
    feet = float(parts[0])
    inches = float (parts[1])
    return {"feet": feet, "inches":inches} # used dictionary beacuse by default it using tuple which is immutable

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    #return f"{feet} feet and {inches} inches is equal to {meters} meters"
    # decoupling means use single value which can be use in other part of code see above return is not that effective
    return meters

parsed = parse(feet_inch)
result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 2:
    print(" Kid is too small to enter ...")
else:
    print(" You are eligible to enter...") 

#print(convert(feet_inch))