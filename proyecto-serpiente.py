import pygame
import random
Game_on=True #para que el juego siga corriendo

pygame.init()

screen = pygame.display.set_mode((700, 400)) #el tamaño de la pantalla

reloj=pygame.time.Clock() #para controlar los fps

Tamaño=20 #tamaño de pixeles de la serpiente

serpiente=[(340,200)]

direccion=(Tamaño,0) #la dirección inicial de la serpiente

while Game_on: #para mantener el juego corriendo
   
   
    for event in pygame.event.get():
        
        
        
        if event.type == pygame.QUIT:
            Game_on=False  #hasta que se cierre la ventana
            
            
            
        if event.type == pygame.KEYDOWN: #para el movimiento de la serpiente y lee las flechas del teclado
            print(pygame.key.name(event.key))
            if event.key==pygame.K_UP and direccion!=(0,Tamaño):
                direccion=(0,-Tamaño)
            if event.key==pygame.K_DOWN and direccion!=(0,-Tamaño):
                direccion=(0,Tamaño)
            if event.key==pygame.K_LEFT and direccion!=(Tamaño,0):
                direccion=(-Tamaño,0)
            if event.key==pygame.K_RIGHT and direccion!=(-Tamaño,0):
                direccion=(Tamaño,0)
            
    
    #dibujar la serpiente
    cabeza=serpiente[0]
    x=cabeza[0]+direccion[0]
    y=cabeza[1]+direccion[1] #nueva posicion de la cabeza de la serpiente
    if x<0:
        Game_on=False
    if x>700-Tamaño:
        Game_on=False
    if y<0:
        Game_on=False
    if y>400-Tamaño:
        Game_on=False
    serpiente.insert(0, (x, y))
    serpiente.pop()
    screen.fill((20, 20, 20)) 
    for segmento in serpiente:
        pygame.draw.rect(screen, (50, 150, 255), (segmento[0], segmento[1], Tamaño, Tamaño)) #dibuja la serpiente
    pygame.display.flip() 
    reloj.tick(5) #para que el juego corra a 10 ticks por segundo



        
        

pygame.quit()

