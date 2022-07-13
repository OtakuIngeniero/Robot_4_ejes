import string

from pkg_resources import parse_requirements


def empaquetar(Q):
    paquete = ""
    for q in Q:
        
        paquete = paquete + str(q)
        paquete = paquete +  "_"
        
        

    return paquete