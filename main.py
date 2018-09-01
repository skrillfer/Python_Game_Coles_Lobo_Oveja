import modulo

print ("Bienvenido al juego para poder ganar debes pasar")
print ("de un lado a otro a la OVEJA, LOBO, y COLES\n")

print ("1. Solo un movimiento a la vez")
print ("2. Si la oveja y el lobo se encuentran solos de un lado")
print ("el lobo se la comera y pierdes el juego")

print ("3. Si la oveja y las coles se encuentran solos de un lado")
print ("la oveja se la comera las COLES y pierdes el juego")

tecla = input ('\nPRESIONA El numero 1 y luego LA TECLA ENTER PARA COMENZAR EL JUEGO:\n')



while(tecla!="1"):
  tecla = input ('\nPRESIONA El numero 1 y luego LA TECLA ENTER PARA COMENZAR EL JUEGO\n')

SALTAR=False
LADO = 2 # LADO=1 (Izquierdo) y LADO=2 (Derecho)
NUM_MOVIMIENTOS = 0
DERECHO = ["OVEJA","LOBO","COLES"]
IZQUIERDO = ["","",""]


LISTA_ACTUAL = DERECHO;

while(modulo.puede_continuar(LADO,DERECHO,IZQUIERDO)):
  if modulo.si_ha_ganado(IZQUIERDO):
    print("Felicidades HAS GANADO EL JUEGO!!! :D\n")
    modulo.mostrar_objetos(LADO,DERECHO,IZQUIERDO)
    SALTAR=True
    break;

  modulo.mostrar_objetos(LADO,DERECHO,IZQUIERDO)
  #Se le pide al jugador seleccionar un objeto
  modulo.pedir_seleccion(LADO,DERECHO,IZQUIERDO)
  tecla = input()

  while( ( int(tecla)<0 or int(tecla)>3) or not (modulo.existe_seleccionado(int(tecla),LISTA_ACTUAL))
  ):
    tecla = input("Numero:"+tecla+" de Objeto Inexistente, ingresa de nuevo el numero:\n")
  
  if int(tecla)==0: # ENTONCES QUIERE CAMBIAR DE LADO
    LADO = modulo.cambiar_lado(LADO)
    LISTA_ACTUAL = modulo.cambiar_lista_actual(LADO,DERECHO,IZQUIERDO)
    print("\nSe ha Cambiado de Lado!!!\n")
    #modulo.mostrar_objetos(LADO,DERECHO,IZQUIERDO)
  else:
    #Ahora se hace el movimiento
    #Cambio el LADO
    LADO = modulo.cambiar_lado(LADO)
    #muestro el mensaje
    mensaje = "Se hara el movimiento de " + LISTA_ACTUAL[int(tecla)-1]
    mensaje += " hacia el lado " + modulo.obtener_nombre_lado(LADO)
    print(mensaje)

    #cambio la lista al lado correspondiente
    # si Lado=1 lista del lado IZQUIERDO
    # si Lado=2 lista del lado DERECHO
    LISTA_ANTERIOR = LISTA_ACTUAL
    LISTA_ACTUAL = modulo.cambiar_lista_actual(LADO,DERECHO,IZQUIERDO)
    modulo.hacer_movimiento(int(tecla),LISTA_ANTERIOR,LISTA_ACTUAL)
    #modulo.mostrar_objetos(LADO,DERECHO,IZQUIERDO)

if not SALTAR:
  print(":( HAS PERDIDO, Juega de Nuevo")
print("==   JUEGO TERMINADO   == ")