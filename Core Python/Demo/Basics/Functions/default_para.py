def emp(id, name = 'abc', sal = 1000, dept = 'Back office'):
    print('ID', id)
    print('NAME', name)
    print('SALARY', sal)
    print('DEPARTMENT', dept)

    print('##########################')

emp(101, 'ABC', 50000)
emp(102, 'XYZ', 80000, 'IT')
emp(103, 'CDE')

# -----------------------------------
# Output
# ID 101
# NAME ABC
# SALARY 50000
# DEPARTMENT Back office
# ##########################
# ID 102
# NAME XYZ
# SALARY 80000
# DEPARTMENT IT
# ##########################
# ID 103
# NAME CDE
# SALARY 1000
# DEPARTMENT Back office
# ##########################