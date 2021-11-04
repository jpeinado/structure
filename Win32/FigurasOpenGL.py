'''
title: programa que dibuja un rectangulo y un triangulo usando la libreria OpenGL
Autor: Juan Carlos Peinado Pereira
Version : 1.0
Leguaje : Python
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400   

def draw_triangle(x, y, width, height):
    glBegin(GL_TRIANGLE_STRIP)
    glVertex2f(x,y)
    glVertex2f(x - width, y - height)
    glVertex2f(x + width, y - height)
    glEnd()

def draw_rect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle                            # window size

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
   
    # ToDo draw rectangle
    refresh2d(width, height)                           # set mode to 2d
    
    #gluPerspective(45.0, 300, 200)   
    glScaled(0.3,0.3,0.3)
    glColor3f(0.0, 2.0, 1.0)                           # set color to blue
    draw_rect(300, 100, 100, 100)
    draw_triangle(100,100,200,200)
   
    glutSwapBuffers()                                  # important for double buffering
   

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()              