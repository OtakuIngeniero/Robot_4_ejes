from robot_t import *


Robot = robot()
Robot._home = [200,0,100,0]
Robot.A_base[2,3] = 95
Robot.A_herr[0,3] = 35
Robot.A_herr[2,3] = -135
Robot.inicar()

input("start")

Robot.moveJ([0,-200,100,0])
time.sleep(0.9)
Robot.moveL([0,-200,40,0],1)

for i in range(0,8,1):
    time.sleep(0.2)
    Robot.moveJ([40,-220,40,0])
    time.sleep(0.2)
    Robot.moveJ([70,-200,40,0])
    time.sleep(0.2)
    Robot.moveJ([40,-180,40,0])
    time.sleep(0.2)
    Robot.moveJ([0,-200,40,0])

time.sleep(0.7)
Robot.moveL([0,-200,100,0],1)
time.sleep(0.7)
Robot.homeJ()
time.sleep(2)
Robot.shutdown()