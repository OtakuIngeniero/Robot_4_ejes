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
import re

Robot = robot()

m=Robot.dir_cinematics([0,-pi/2,pi/2,0])
pprint(m)

#pprint(m*m.inv())
#pprint(m)

Q = Robot.inv_cinematics(m)



"""from mpmath import *
print (degrees(Q[0]))
print (degrees(Q[1]))
print (degrees(Q[1]))
print (degrees(Q[2]))
print (degrees(Q[3]))"""


#pprint(Robot.A04sym())

pprint(Robot.dir_cinematics(Q))
pprint(Q)
Robot.inicar()
Robot.stream(Q)
pprint(Q)

step = 2
speed = 10
"""for i in  range(50,250,step):
    m[0,3] = 0
    m[1,3] = i
    m[2,3] = 0
    
    Q = Robot.inv_cinematics(m)
    pprint(Robot.dir_cinematics(Q))
    Robot.stream(Q)
    time.sleep(1/speed)"""
pose = [90,90,90,0]
s1 = "50,0,0,0"

while s1 != "end":
    
    pose=[int(x) for x in re.findall(r'[^,.]+', ''.join(s1.split()))]
    if len(pose) != 4:
        pose = [90,90,90,0]
    m = P2A(pose)
    V = Robot.inv_cinematics(m)
    #pprint(sympy.simplify(Robot.dir_cinematics(V)))
    Robot.stream(V)
    #pprint(sympy.simplify(V))
    pprint(Robot.dh2rob(V))
    s1 = input("pose = ")
    

Robot.shutdown()
#msym = Robot.A04sym()
#mrem = Subs(msym,symbols('th1,th2,th3,th4'),[pi/2,-pi/2,pi/2,-pi/2])
#pprint (simplify(mrem))
#print ("finite")
"""Robot.inicar()
step = 1
speed = 10
for ts in  range(1,5,1):
    for i in  range(55,121,step):
        Robot.stream([i,i,i,0])

        time.sleep(1/speed)

    for i in  range(0,120-55,step):
        Robot.stream([120-i,120-i,120-i,0])

        time.sleep(1/speed)

Robot.shutdown()"""


