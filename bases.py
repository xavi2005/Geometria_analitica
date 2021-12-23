import time
from time import sleep
#Aquesta opció descarta la posibilitat que no coneiguis els eixos,x i y
#Calcula mitjançant la equació de calcular_vector_director(self)
#També s'introduiex una equació que mitjançant el mètode de reducció es pot arribar a trobar els components de la combinació lineal de les bases

class Base():
  def __init__(self,v11,v12,v21,v22,h,p):
    self.v11 = v11
    self.v12 = v12
    self.v21 = v21
    self.v22 = v22
    self.v1 = [v11,v12]
    self.v2 = [v21,v22]
    self.Base = [self.v1,self.v2]
    self.h = h
    self.p = p
    self.hp  = [self.h,self.p]
#Aquesta funció només es efectiva en el primer cas on es demanen les x i y  
  def imprimir_dades(self):
    print(f"->Partim d'una B = {self.Base}...")
    time.sleep(2)
    print(f"->Detectem els vectors v = {self.v1} i w = {self.v2}")
    time.sleep(2)
    print(f"->La combinació lineal on h = {self.h} i on p = {self.p}")
    time.sleep(2)
    print("->Processant expressió final...")
    time.sleep(2)
    print("->Equació obtinguda")
    print(f"[x,y] = {self.h}*{self.v1} + {self.p}*{self.v2} ")
    time.sleep(2)
    print("->Separant els eixos...")
    time.sleep(2)
    print("->Calculant...")
    time.sleep(2)
    print("->Proces finalitzat.")
#Calcula els eixos x i y a través de la base digitada per l'usuari, també inclou la combinació lineal de dos components dits(h,p)
  def calcular_vector_director(self):
    x = self.h*self.v11 + self.p*self.v21
    y = self.h*self.v12 + self.p*self.v22
    print(f"x = {x} i y = {y}")
    return x,y
    
  
#Com que es tracta d'una equació utilitzarem el mètode de 
# reduccio 
#Defim g com una variable que guardarà la relació de les dues equacions perquè la suma doni zero.

  def calcular_components(self,x,y):
    g =(self.v12/self.v11)*-1
    new_var_x = x * g
    new_var_v21= self.v21 * g
    new_var_v11 = self.v11 * g
    new_eq_1 = new_var_x + y
    new_eq_2 = new_var_21 + self.v22  
    f = new_var_v11 + self.v12 
#Aquesta ha de ser zero ja que hem buscat la relació de dos coeficients
    if f == 0:
      pass
    else: 
      return False
    
    p = new_eq_1 / new_eq_2
    h = (y - self.v22*p)/self.v12
    print(f"La combinació lineal és de component h = {h} i de component p = {p}")
    return h,p
    
  
  
    
    
    
    
    
    
    
