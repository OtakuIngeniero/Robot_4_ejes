"""import string

from pkg_resources import parse_requirements


def empaquetar(Q):
    paquete = ""
    for q in Q:
        
        paquete = paquete + str(q)
        paquete = paquete +  "."
        
        

    return paquete"""

def empaquetar(Q):
    paquete = "<" + str(Q[0]) + ":" + str(Q[1]) + ":" + str(Q[2]) + ":" + str(Q[3]) + ">"
    return paquete