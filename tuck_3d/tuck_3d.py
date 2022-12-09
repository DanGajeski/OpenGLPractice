from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def draw():
	xrot = 45
	yrot = 45
	glClear(GL_COLOR_BUFFER_BIT)
	#glVertex2d(100,100)
	glRotatef(xrot, 1.0, 0.0, 0.0)
	glRotatef(yrot, 0.0, 1.0, 0.0)
	#glBegin(GL_POINTS)
	glutWireCube(0.7)
	#glVertex2i(100,100)
	#glEnd()
	#glutWireCube(1.0)
	#glutWireDodecahedron()
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1024, 512)
glutInitWindowPosition(0, 100)

glutCreateWindow("Ol' Tuck")

glutDisplayFunc(draw)
glutMainLoop()