'''from sympy import false, true
from sympy.matrices import *
from sympy.interactive.printing import init_printing
from sympy import *
from robotito import *
from robot_t import robot
#from sympy import init_session
#init_session()
init_printing()

A = Matrix([[1,2],[3,4]])
B = Matrix([[1,1],[1,1]])
C = A * B
print(pretty(C))
pprint(A.row(0))



Robot=robotito()
D = Robot.unmetodo()
pprint(D)
unafuncion()
myRobot = robot()
pprint(myRobot.dir_cinematics(1))

pprint(A[0,0])
'''
from sympy import *
from A_a2b import A_a2b
from robot_t import *

Robot = robot()

m=Robot.dir_cinematics([pi,-pi/2,pi/2,0])
pprint(m)

#pprint(m*m.inv())
#pprint(m)

Q = Robot.inv_cinematics(m)
pprint(Q)

"""from mpmath import *
print (degrees(Q[0]))
print (degrees(Q[1]))
print (degrees(Q[1]))
print (degrees(Q[2]))
print (degrees(Q[3]))"""


#pprint(Robot.A04sym())

pprint(Robot.dir_cinematics(Q))
#msym = Robot.A04sym()
#mrem = Subs(msym,symbols('th1,th2,th3,th4'),[pi/2,-pi/2,pi/2,-pi/2])
#pprint (simplify(mrem))
#print ("finite")
Robot.inicar()

for ts in  range(10,1000,100):
    for i in  range(45,121,1):
        Robot.stream([i,i,i,0])
        time.sleep(1/ts)

    for i in  range(0,120-45,1):
        Robot.stream([120-i,120-i,120-i,0])
        time.sleep(1/ts)

Robot.stream([120,120,120,0])
time.sleep(1)
Robot.stream([45,45,45,0])
#Robot.stream([10,10,10,0])
Robot.shutdown()


