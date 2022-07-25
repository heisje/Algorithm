def eap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return f'{year}년은 윤년입니다.'
    return f'{year}년은 윤년이 아닙니다.'

print(eap_year(2021))
print(eap_year(2020))