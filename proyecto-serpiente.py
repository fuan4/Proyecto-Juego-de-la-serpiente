import pygame
import random
Game_on=True #para que el juego siga corriendo
Iniciar= False
perder=False 
Tamaño=20 #tamaño de pixeles de la serpiente
Puntuacion=0
Record=0
Comida=(random.randrange(0,700,Tamaño),random.randrange(0,400,Tamaño)) #para la comida de la serpiente
pygame.init()

screen = pygame.display.set_mode((700, 400)) #el tamaño de la pantalla

texto=pygame.font.SysFont("Arial", 30) #para el texto de la pantalla

mensaje=texto.render("Presione cualquier tecla para iniciar",True,(255,255,255)) #mensaje de inicio

mnsjlose=texto.render("Perdiste, presiona R para reiniciar",True,(255,255,255))

posicion_mnsjlose=mnsjlose.get_rect(center=(350, 200))

posicion_mensaje=mensaje.get_rect(center=(350, 200))

reloj=pygame.time.Clock() #para controlar los fps

Tamaño=20 #tamaño de pixeles de la serpiente

serpiente=[(340,200)]

direccion=(Tamaño,0) #la dirección inicial de la serpiente

while Game_on: #para mantener el juego corriendo

   
   
    for event in pygame.event.get():
        
        
        
        if event.type == pygame.QUIT:
            Game_on=False  #hasta que se cierre la ventana
            
            
            
        if event.type == pygame.KEYDOWN: #para el movimiento de la serpiente y lee las flechas del teclado
            if perder == True and event.key == pygame.K_r: #reiniciar con la tecla R 
                perder= False
                Iniciar = True
                Puntuacion=0
                serpiente=[(340,200)]
                direccion=(Tamaño,0)
                Comida=(random.randrange(0,700,Tamaño),random.randrange(0,400,Tamaño))
            if Iniciar == False:
                Iniciar = True
            print(pygame.key.name(event.key))  # el movimiento 
            if event.key==pygame.K_UP and direccion!=(0,Tamaño):
                direccion=(0,-Tamaño)
            if event.key==pygame.K_DOWN and direccion!=(0,-Tamaño):
                direccion=(0,Tamaño)
            if event.key==pygame.K_LEFT and direccion!=(Tamaño,0):
                direccion=(-Tamaño,0)
            if event.key==pygame.K_RIGHT and direccion!=(-Tamaño,0):
                direccion=(Tamaño,0)
            
    
    #dibujar la serpiente
    if Iniciar == True and perder==False:
        cabeza=serpiente[0]
        x=cabeza[0]+direccion[0]
        y=cabeza[1]+direccion[1]
        if x<0 or x>700-Tamaño or y<0 or y>400-Tamaño or (x,y) in serpiente: # para los limites del juego
            perder=True
        else:
            serpiente.insert(0, (x, y))
            if (x,y) == Comida: # el contador de la puntuación y el record
                Puntuacion += 1
                if Puntuacion > Record:
                    Record = Puntuacion
                Comida = (random.randrange(0, 700, Tamaño), random.randrange(0, 400, Tamaño)) # para dibujar la comida
            else: 
             serpiente.pop()  #elimina el último segmento de la serpiente si no ha comido comida    
    #nueva posicion de la cabeza de la serpiente
    screen.fill((20, 20, 20)) 
    marcador_record=texto.render("Record: "+str(Record),True,(255,255,255)) # dibuja el record en la pantalla
    screen.blit(marcador_record, (550,10))
    marcador_puntuacion=texto.render("Puntuacion: "+str(Puntuacion),True,(255,255,255)) #dibuja la puntuación en la pantalla
    screen.blit(marcador_puntuacion, (10,10))
    pygame.draw.rect(screen, (255,0,0), (Comida[0],Comida[1],Tamaño,Tamaño)) # dibuja la comida
    for segmento in serpiente:
        pygame.draw.rect(screen, (50, 150, 255), (segmento[0], segmento[1], Tamaño, Tamaño)) #dibuja la serpiente
    if Iniciar == False:
        screen.blit(mensaje, posicion_mensaje)
    if perder == True:
        screen.blit(mnsjlose, posicion_mnsjlose)
    pygame.display.flip() 
    reloj.tick(10) #para que el juego corra a 10 ticks por segundo

pygame.quit()

