import sys
r = int(sys.argv[1])
def leap_year(year):
    if (year%4)==0:
        if (year%100)==0:
            if (year%400)==0:
                return year
            else:
                pass
        else:
            return year
    else:
        pass
print(leap_year(r))
