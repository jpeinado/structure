'''
Name proyect : Manejo de graficas con OpenGl
Autor: Juan Carlos Peinado Pereira
Date: 2021/05/23
Version: beta 1
'''
# Librerias graficas opengl para uso en python
import pygame
from pygame.locals import *

#import OpenGl
#from OpenGl.GL import *
from OpenGL.GL import *
from OpenGL.GLU import *
#from pyopengl.GL import *
#from pyopengl.GLU import *
# Definicion de estructuras para graficar

verticies =(
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
)
edges =(
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (1,1,1)
)
def cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        x += 1
        glColor3fv(colors[x])
        for vertex in surface:
            glVertex3fv(verticies[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
def main():
    pygame.init()
    
    x = 0 
    y = 0 
    z = 0 
    
    display = (800,600)
    pygame.display.set_mode(display,pygame.DOUBLEBUF|pygame.OPENGL)
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    
    
    gluPerspective(45,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0.0,0.0,-5)
    glRotatef(0,0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_a:
                    x = 0.1
                elif event.key == pygame.K_d:
                    x = -0.1
                elif event.key == pygame.K_w:
                    z = 0.1
                elif event.key == pygame.K_s:
                    z = -0.1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and x > 0:
                    x = 0
                elif event.key == pygame.K_d and x < 0:
                    x = 0 
                if event.key == pygame.K_w and z > 0:
                    z = 0
                if event.key == pygame.K_s and z < 0:
                    z = 0
                    
        glTranslatef(x,y,z)
        glColor3f(0.0, 2.0, 1.0)        
        glRotatef(1,2,3,4)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)
main()

