import time

# Record the start time
start_time = time.time()


print("Welcome to the program that tells you if an year is a leap year!")
print("")
print("Starting on year 0, how many years would you like to calculate?")
print("")

years_to_calculate = int(input("Number of years: ?"))
count = 0

for year in range(years_to_calculate+1):
    if year % 400 == 0:
        print(f"{year} is a leap year!")
        count += 1
    elif year % 100 == 0:
        print(f"{year} is not a leap year.")
    elif year % 4 == 0:
        print(f"{year} is a leap year!")
        count += 1
    else:
        print(f"{year} is not a leap year")

print(f"{count} leap years counted in the space of {years_to_calculate} years.")


# Record the end time
end_time = time.time()
# Calculate the elapsed time 
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
