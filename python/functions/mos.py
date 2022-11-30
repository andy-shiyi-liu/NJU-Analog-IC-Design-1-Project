import math

def Vgs2Id(Vgs:float, Vth:float, K:float, S:float):
    return (K * S * ((Vgs - Vth)**2))/2

def Id2Von(Id:float, K:float, S:float):
    return math.sqrt(2 * Id / (K * S))

def Id2Vgs(Id:float, Vth:float, K:float, S:float):
    return Id2Von(Id, K, S) + Vth

def Id2gm(Id:float, K:float, S:float):
    return math.sqrt(2 * K * S * Id)