#Leapyear
"""
year ℅ 4==0&
year % 100!=0/
year % 400==0
"""
def is leap year(year):
if(year℅ 4==0and year℅100!=0)or year℅400==0:
  return True
else:
  return False
year=2012
if is leapyear(year):
  print('{}is not a leapyear.'.format(year))