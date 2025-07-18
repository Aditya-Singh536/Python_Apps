principle = input("Enter the principle:")
while str(principle).isdecimal():
    principle = float(principle)
    while principle <= 0:
        principle = float(input("Enter the principle:"))
    else:
        principle = float(principle)
        break
else:
    raise Exception("**Invalid Input**")

rate = input("Enter the rate of interest:")
while str(rate).isdecimal():
    rate = float(rate)
    while rate <= 0:
        rate = float(input("Enter the rate of interest:"))
    else:
        rate = float(rate)
        break
else:
    raise Exception("**Invalid Input**")

time = input("Enter the time of interest in years:")
while str(time).isdecimal():
    time = float(time)
    while time <= 0:
        time = float(input("Enter the time of interest in years:"))
    else:
        time = float(time)
        break
else:
    raise Exception("**Invalid Input**")


result = principle * (1 + rate / 100) ** time

print(f"\nBalance after {time} year/s:${result:.2f}")
