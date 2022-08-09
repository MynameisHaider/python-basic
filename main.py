# PYTHON PACKAGES
# from mainfolder import folder/module
#then .function()
#this programe i.e main.py is used with subfolder named calc, where other modules are defined.

from calc import add,sub,mult
from calc import area,factorial
print(add.add(2,3))
print(sub.sub(2,3))
print(mult.mult(2,3))
print(add.add3(5,5,5))
print(area.rectangle(4,5))
print("factorial: ",factorial.rfact(5))

