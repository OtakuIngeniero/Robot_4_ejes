from numbers import Real
from sympy import *
import sympy
from A_a2b import P2A, A_a2b
import serial,time
from empaquetador import empaquetar

class robot:
    _pos = [0,0,0,0]
    _d = [0,0,0,0,0]
    _alfa = [-pi/2,0,0,pi/2,0]
    _a = [0,115,117.62,25,0]
    _vth_max = (5/3)*pi
    _home = eye(4)

    Ts = 1*10**(-3)
    offsets_motores = [0,0,0,0]
    theta = [0,0,0,0]
    A04 = eye(4)
    A_base = eye(4)
    A_herr = eye(4)
    puerto = 'COM4'
    brate = 115200
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
    # Metodo que me calcula la cinematica directa del robot con los Q pasados por argumento
    # me devuelve la transformacion entre la base del robot y la herramienta, pero tambien guarda el A04
    # Q0 theta_1
    # Q1 theta_2
    # Q2 theta_3
    # Q3 theta_4
    def dir_cinematics(self,Q):   

        A = eye(4) #inicializo A como la matriz de rototranslacion nula alias identidad

        A[0,0] = -sin(Q[0])*sin(Q[3]) + cos(Q[0])*cos(Q[3])
        A[0,1] = -sin(Q[0])*cos(Q[3]) - cos(Q[0])*sin(Q[3])
        A[0,2] = 0
        A[0,3] = (self._a[1]*cos(Q[1]) + self._a[2]*cos(Q[1]+Q[2]) + self._a[3])*cos(Q[0])

        A[1,0] =  sin(Q[0])*cos(Q[3]) + cos(Q[0])*sin(Q[3])
        A[1,1] = -sin(Q[0])*sin(Q[3]) + cos(Q[0])*cos(Q[3])
        A[1,2] = 0
        A[1,3] = (self._a[1]*cos(Q[1]) + self._a[2]*cos(Q[1]+Q[2]) + self._a[3])*sin(Q[0])

        A[2,3] = -self._a[1]*sin(Q[1]) - self._a[2]*sin(Q[1]+Q[2])


        return self.A_base * A * self.A_herr

#-------------------------------------------------------------------------------------------------------
# Este metodo me devuelve la matriz A04 expresada en funcion de los th
    def A04sym(self):
        A04_sym = eye(4)
        Q = symbols('th1,th2,th3,thni,th4')

        for  i in  range(0,5,1):
            A04_sym = A04_sym * A_a2b(self._d[i],Q[i],self._alfa[i],self._a[i])
        
        A04_sym = sympy.simplify( A04_sym )
        A04_sym = Subs(A04_sym,Q[3],-(Q[1]+Q[2]))
        return sympy.simplify( A04_sym )
#-------------------------------------------------------------------------------------------------------
    # Metodo que me calcula la cinematica inversa del robot con la Abase-brida (Abb) pasado por argumento
    # me devuelve las posiciones de las articulaciones del robot, este robot por su mecanica tiene siempre
    # solo una configuracion valida (brazo hacia arriba) asi que no es necesario pasarle un vector de 
    # configuracion, pero se lo voy a agregar para generalizar el modelo, cfg=1 es brazo hacia arriba,
    # cfg=-1 es brazo hacia abajo
    # Q0 theta_1
    # Q1 theta_2
    # Q2 theta_3
    # Q3 theta_4
    def inv_cinematics_c(self,Abb,cfg):
        A = self.A_base.inv() * Abb * self.A_herr.inv()
        th = [0,0,0,0]

        th[0] = atan2(A[1,3],cfg*A[0,3]) # calculo th 0
    
        s1=sin(th[0])
        
        c1=cos(th[0])

        s4 = A[1,0]*c1 - A[0,0]*s1 

        if c1 == 0: # uso la expresion que no se rompa por la singularidad de la division
            b = A[1,3]/s1 - self._a[3]
            c4 = -(A[0,1] + s4*c1)/s1
        else:
            b = A[0,3]/c1 - self._a[3]
            c4 = (A[0,0] + s4*s1)/c1

        # calculo th 4     
        th[3] = atan2(s4,c4) 

        c3 = ((b)**2 + A[2,3]**2 - (self._a[1]**2 + self._a[2]**2))/(2*self._a[1]*self._a[2]) # ahora calculo th3
        s3 = sqrt(1-c3**2)
        th[2] = atan2(s3,c3)
        

        # por ultimo calculo th2

        s2=(self._a[2]*(-A[2,3]*c3-b*s3)-self._a[1]*A[2,3])/(b**2 + A[2,3]**2)
        c2=(self._a[2]*(-A[2,3]*s3+b*c3)+self._a[1]*b)/(b**2 + A[2,3]**2)

        th[1] = atan2(s2,c2)

        return th
#-------------------------------------------------------------------------------------------------------
# el mismo metodo pero para no tener que poner siempre el cfg que no se necesita 
# (el brazo siemre mira arriba)
    def inv_cinematics(self,Abb):
        return self.inv_cinematics_c(Abb,1)
#-------------------------------------------------------------------------------------------------------
# metodo que inicia la posicion del robot y lo manda a home
    def inicar(self):
        self._home = Matrix([[1,0,0,50],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.A04 = self._home
        self._pos = P2A (self.A04)
        self.theta = self.inv_cinematics(self.A04)
        self.arduino = serial.Serial(self.puerto,self.brate)
        time.sleep(2)
#-------------------------------------------------------------------------------------------------------
# metodo que manda al robot a hacer un home
    def homeJ(self,home_speed):
        self.moveJ(self._home,home_speed)
#-------------------------------------------------------------------------------------------------------
# metodo que hace al robot hacer un movimiento joint entre su pose actual y la pose deseada

# por ahora solo voy a devolver los angulos deseados y despues lo hago bien
    def moveJ(self,pose,joint_speed):
        A = P2A(pose)
        Q = self.inv_cinematics(A)
        return Q
#-------------------------------------------------------------------------------------------------------

    def stream(self,Q):
        paquete = empaquetar(Q)
        print (paquete)
        self.arduino.write(paquete.encode())
        #self.arduino.write(b'4')
        return 
    def shutdown(self):
        self.arduino.close()
    