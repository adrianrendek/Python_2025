year = int(input("Year: "))
year_c = year + 1

while True:
    if (year_c % 4 == 0 and year_c % 100 != 0) or (year_c % 400 == 0):
        print(f"The next leap year after {year} is {year_c}")
        break
    year_c += 1



    


