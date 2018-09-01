
def si_ha_ganado(Izquierdo):
  OVEJA = False
  LOBO  = False
  COLES = False
  for x in Izquierdo:
    if x=="OVEJA":
      OVEJA = True
    elif x=="LOBO":
      LOBO = True
    elif x=="COLES":
      COLES = True
  if OVEJA and LOBO and COLES:
    return True
  else:
    return False

def puede_continuar(Lado,Derecho,Izquierdo):
  OVEJA = False
  LOBO  = False
  COLES = False
  for x in Izquierdo:
    if x=="OVEJA":
      OVEJA = True
    elif x=="LOBO":
      LOBO = True
    elif x=="COLES":
      COLES = True

  if OVEJA and LOBO and not COLES and not Lado==1:
    print("Has dejado SOLO A El Lobo y se COMIO a La Oveja\n")
    mostrar_objetos(Lado,Derecho,Izquierdo)
    return False
  elif OVEJA and COLES and not LOBO and not Lado==1:
    print("Has dejado SOLA A La Oveja y se COMIO Las Coles\n")
    mostrar_objetos(Lado,Derecho,Izquierdo)
    return False

  OVEJA = False
  LOBO  = False
  COLES = False
  for x in Derecho:
    if x=="OVEJA":
      OVEJA = True
    elif x=="LOBO":
      LOBO = True
    elif x=="COLES":
      COLES = True

  if OVEJA and LOBO and not COLES and not Lado==2:
    print("Has dejado SOLO A El Lobo y se COMIO a La Oveja\n")
    mostrar_objetos(Lado,Derecho,Izquierdo)
    return False
  elif OVEJA and COLES and not LOBO and not Lado==2:
    print("Has dejado SOLA A La Oveja y se COMIO Las Coles\n")
    mostrar_objetos(Lado,Derecho,Izquierdo)
    return False
  return True

def mostrar_objetos(Lado,Derecho,Izquierdo):
  linea  = "=============================="
  linea2  = "______________________________"
  imagen = linea + linea + "\n"
  for x in Izquierdo:
    imagen += "["+ x + "]"
  imagen += "\t\t\t\t\t"

  for y in Derecho:
    imagen += "["+ y + "]"
  
  imagen += "\n" + linea2 + linea2+"\n"
  if Lado==1:
    imagen +="[_(Lancha)_]"
  else:
    imagen += "\t\t\t\t\t\t"
    imagen +="[_(Lancha)_]"
  imagen += "\n" + linea2 + linea2 + "\n"
  print(imagen)

def pedir_seleccion(Lado,Derecho,Izquierdo):
  contador = 1
  mensaje ="Selecciona un objeto del lado "
  if Lado==2:
    mensaje += "DERECHO "
    mensaje += "ingresando el numero:\n"
    mensaje += "-->Ingresa 0 para cambiar de LADO<--\n"
    for x in Derecho:
      if(x!=""):
        mensaje +=str(contador) + "- "+ x + "\n"
        contador=contador+1
      else:
        contador=contador+1
  else:
    mensaje += "IZQUIERDO "
    mensaje += "ingresando el numero:\n"
    mensaje += "-->Ingresa 0 para cambiar de LADO<--\n"
    for x in Izquierdo:
      if(x!=""):
        mensaje +=str(contador) + "- "+ x + "\n"
        contador=contador+1
      else:
        contador=contador+1
  print(mensaje)
  
def existe_seleccionado(posicion,lista):
  if posicion==0:
    return True

  if (posicion-1) < len(lista):
    if lista[posicion-1] != "":
      return True
    else:
      return False
  else:
    return False

def obtener_nombre_lado(Lado):
  if Lado==1:
    return "Izquierdo"
  else:
    return "Derecho" 

def cambiar_lado(Lado):
  if Lado==1:#Lado Izquierdo
    return 2
  else:#Lado derecho
    return 1

def cambiar_lista_actual(Lado,Derecho,Izquierdo):
  if Lado==1:#Lado Izquierdo
    return Izquierdo
  else:#Lado derecho
    return Derecho

def hacer_movimiento(posicion,lista_anterior,lista_actual):
  lista_actual[posicion-1]=lista_anterior[posicion-1]
  lista_anterior[posicion-1]=""