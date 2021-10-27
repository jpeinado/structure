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

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display,pygame.DOUBLEBUF|pygame.OPENGL)
    gluPerspective(45,(display[0]/display[1]),0.1,50.0)
    glTranslatef(0.0,0.0,-5)
    glRotatef(0,0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1,3,1,1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)
main()

