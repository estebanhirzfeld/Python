def leap_year_check(year):
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            return print(year,'Fue año bisiesto')
        else:
            return print(year,'No fue un año bisiesto')

leap_year_check(1900)