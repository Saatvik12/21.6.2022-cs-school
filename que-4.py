#4th code
hours = int(input('enter the hours worked: '))
wage = int(input('enter the hourly wage: '))
if hours<40:
  total = hours*wage
elif hours>=40:
  total = 2*wage
print('your wage is', total)
