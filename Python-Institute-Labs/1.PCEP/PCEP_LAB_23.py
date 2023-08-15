def is_year_leap(year):
    if year % 4 != 0:  # Si el año no es divisible entre 4, entonces no es bisiesto
        return False
    elif year % 100 != 0:  # Si el año no es divisible entre 100, es bisiesto
        return True
    elif year % 400 != 0:  # Si el año no es divisible entre 400, entonces no es bisiesto
        return False
    else:  # Si el año es divisible entre 400, es bisiesto
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
