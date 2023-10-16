from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500, 500

rainy = 250  
rainydown = 240  
speed = 5
x = -250
y = -250
time = ""
pressed = "n"

class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

def draw_points(x, y, s):
    glPointSize(s)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()

def keyboardListener(key, x, y):

    global pressed
    if key==b'd':
        pressed = "d"
        print("Day")
    if key==b'n':
        pressed = "n"
        print("Night")

    glutPostRedisplay()

def specialKeyListener(key, k, j):
    global x,y, rainy, rainydown
    if key == GLUT_KEY_LEFT:
        rainy = 250  
        rainydown = 240
        if y >=-259:
            y -=1   
        print("Rain Left")
    if key == GLUT_KEY_RIGHT:
        rainy = 250  
        rainydown = 240
        if y <=-241:
            y +=1   
        print("Rain Right")
    glutPostRedisplay()

def display():
    global time
    # //clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if time == "night":
        glClearColor(0, 0, 0, 0)  # //color black
    else:
        glClearColor(1.0, 1.0, 1.0, 0.0)  # //color white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # //load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    # //initialize the matrix
    glLoadIdentity()
    # //now give three info
    # //1. where is the camera (viewer)?
    # //2. where is the camera looking?
    # //3. Which direction is the camera's UP direction?
    gluLookAt(0, 0, 200,	0, 0, 0,	0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    # drawAxes()
    # drawShapes()

    glLineWidth(3)
    if time == "night":
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    # house body
    glVertex2d(180, 0)
    glVertex2d(180, -180)
    glVertex2d(180, -180)
    glVertex2d(-180, -180)
    glVertex2d(-180, -180)
    glVertex2d(-180, 0)
    glVertex2d(-180, 0)
    glVertex2d(180, -0)
    # window right
    glVertex2d(70, -30)
    glVertex2d(130, -30)
    glVertex2d(130, -30)
    glVertex2d(130, -90)
    glVertex2d(130, -90)
    glVertex2d(70, -90)
    glVertex2d(70, -90)
    glVertex2d(70, -30)
    # window left
    glVertex2d(-70, -30)
    glVertex2d(-130, -30)
    glVertex2d(-130, -30)
    glVertex2d(-130, -90)
    glVertex2d(-130, -90)
    glVertex2d(-70, -90)
    glVertex2d(-70, -90)
    glVertex2d(-70, -30)
    # door
    glVertex2d(30, -180)
    glVertex2d(30, -60)
    glVertex2d(30, -60)
    glVertex2d(-30, -60)
    glVertex2d(-30, -60)
    glVertex2d(-30, -180)

    glEnd()

    # door handle
    draw_points(20, -115, 5)

    # house roof
    if time == "night":
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(190, 0)
    glVertex2d(0, 130)
    glVertex2d(-190, 0)
    glEnd()

    # rain
    glLineWidth(1)
    glBegin(GL_LINES)


    global x,y, rainy, rainydown
    store = y
    for i in range(0, 220):
        # if i % 2 == 0:
        #     glVertex2d(x, rainy)
        #     glVertex2d(x, rainydown)
        #     x+=25
        # else:
        #     glVertex2d(x, rainy-10)
        #     glVertex2d(x, rainydown-10)
        #     x+=25
        if y == -250:
            if i % 2 == 0:
                if x<=250:
                    glVertex2d(x, rainy)
                    glVertex2d(x, rainydown)

                    x+=25
                else:
                    x=-225
                    rainy -= 50
                    rainydown -= 50
                    glVertex2d(-250, rainy)
                    glVertex2d(-250, rainydown)

            else:
                if x<=250:
                    glVertex2d(x, rainy-25)
                    glVertex2d(x, rainydown-25)
                    x+=25
                else:
                    x=-250
                    rainy -= 50
                    rainydown -= 50
        else:
            if i % 2 == 0:
                if x<=250:
                    glVertex2d(x, rainy)
                    glVertex2d(y, rainydown)

                    x+=25
                    y+=25
                else:
                    x= 225
                    y= store-25
                    rainy -= 50
                    rainydown -= 50
                    glVertex2d(-250, rainy)
                    glVertex2d(-270, rainydown)
            else:
                if x<=250:
                    glVertex2d(x, rainy-25)
                    glVertex2d(y, rainydown-25)
                    x+=25
                    y+=25
                else:
                    x=-250
                    y= store
                    rainy -= 50
                    rainydown -= 50

    glEnd()


    glutSwapBuffers()

def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global time, x, y, rainy, rainydown,speed, pressed
    if pressed == "n":
        time = "night"
    else:
        time = "day"
   
    rainy = (rainy - speed + 250) % 500 - 250
    rainydown = (rainydown - speed + 250) % 500 - 250

def init():
    # //clear the screen
    glClearColor(0, 0, 0, 0)
    # //load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    # //initialize the matrix
    glLoadIdentity()
    # //give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    # //near distance
    # //far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
# //Depth, Double buffer, RGB color
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Building a House in Rainfall")
init()

glutDisplayFunc(display)  # display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

glutMainLoop()  # The main loop of OpenGL