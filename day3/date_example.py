from datetime import date

d1 = date.today()
print (d1)
#ISO format is yyyy-mm-dd, try mm > 12 or day > 31
d2 = date.fromisoformat('2019-01-24')
print (d2)
d3=date(2020,3,1) #march 1st
print (d3)
print( abs((d1 - d2).days) )
print (abs(d2-d3))
