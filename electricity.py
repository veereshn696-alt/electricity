import sys
if len(sys.argv)!=1:
  print("usage : python script.py <unit>")
  unit=10
else :
  script_name=sys.argv[0]
  unit=int(sys.argv[1])
perunit=5
bill=unit*perunit
print("unit =",unit)
print("perunit =",perunit)
print("bill =",bill)
