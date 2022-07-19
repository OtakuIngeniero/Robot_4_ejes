from robot_t import *


Robot = robot()
Robot.inicar()
time.sleep(2)
Robot.moveJ([200,0,50,0])
time.sleep(1)

for i in range(0,5,1):
    Robot.moveL([200,0,0,0],1)
    time.sleep(0.7)
    Robot.moveL([200,0,50,0],1)
    time.sleep(0.7)
    Robot.moveJ([0,150,50,0])
    time.sleep(0.7)
    Robot.moveL([0,150,0,0],1)
    time.sleep(0.7)
    Robot.moveL([0,150,50,0],1)
    time.sleep(0.7)
    Robot.moveJ([200,0,50,0])
    time.sleep(0.7)

Robot.homeJ()
Robot.shutdown()


