#include <GL/glut.h>
#include <stdio.h>
#include <iostream>
#include <cmath>
#define GL_PI 3.1415f

bool bCull = 1;
int num = 0;

GLfloat xTran = 0.0f;
GLfloat yTran = 0.0f;
GLfloat xRot = 0.0f;
GLfloat yRot = 0.0f;

void SpecialKeys(int key, int x, int y) {
	if (key == GLUT_KEY_UP)
		xRot -= 2.0f;
	else if (key == GLUT_KEY_DOWN)
		xRot += 2.0f;
	else if (key == GLUT_KEY_LEFT)
		yRot -= 2.0f;
	else if (key == GLUT_KEY_RIGHT)
		yRot += 2.0f;

	if (xRot > 360.0f)
		xRot -= 360.0f;
	if (xRot < 0.0f)
		xRot += 360.0f;
	if (yRot > 360.0f)
		yRot -= 360.0f;
	if (yRot < 0.0f)
		yRot += 360.0f;

	glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y) {
	if (key == 'a')
		xTran -= 2.0f;
	else if (key == 'd')
		xTran += 2.0f;
	else if (key == 'w')
		yTran += 2.0f;
	else if (key == 's')
		yTran -= 2.0f;
	else if (key == '1')
		num = 1;
	else if (key == '2')
		num = 2;
	else if (key == '3')
		num = 3;
	else if (key == '4')
		num = 4;
	else if (key == '5')
		num = 5;
	else if (key == '6')
		num = 6;
	else if (key == '7')
		num = 7;
	else if (key == '8')
		num = 8; 
	glutPostRedisplay();
}

void RenderScene(void) {

	int cnt = 0;
	glClear(GL_COLOR_BUFFER_BIT);

	if (bCull)
		glEnable(GL_CULL_FACE);
	else
		glDisable(GL_CULL_FACE);

	glPushMatrix();
	glRotatef(xRot, 1.0f, 0.0f, 0.0f);
	glRotatef(yRot, 0.0f, 1.0f, 0.0f);

	glTranslatef(xTran, yTran, 0.0f);

	GLfloat x, y, angle;
	int iPivot = 1;
	glBegin(GL_TRIANGLE_FAN);
	glVertex2f(0.0f, 0.0f);

	for (angle = 0.0f; angle < (2.05f * GL_PI); angle += (GL_PI / 4.0f)) {

		if (cnt == num+1)
			break;

		x = 50.0f * cos(angle);
		y = 50.0f * sin(angle);

		if ((iPivot % 2) == 0)
			glColor3f(0.0f, 1.0f, 0.0f);
		else
			glColor3f(1.0f, 0.0f, 0.0f);

		cnt++;
		iPivot++;
		glVertex2f(x, y);
	}
	glEnd();
	glPopMatrix();
	glutSwapBuffers();
}

void SetupRC(void) {
	// std::cout << "SetupRC" << std::endl;
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	glShadeModel(GL_FLAT);

}

void ChangeSize(GLsizei w, GLsizei h) {
	// std::cout << "w = " << w << " " << " h = " << h << std::endl;
	// std::cout << "ChangeSize" << std::endl;

	GLint nRange = 100.0f;
	GLfloat aspectRatio;
	if (h == 0) {
		h = 1;
	}
	glViewport(0, 0, w, h);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	aspectRatio = (GLfloat)w / (GLfloat)h;
	if (w <= h)
		glOrtho(-nRange, nRange, -nRange / aspectRatio, nRange / aspectRatio, nRange, -nRange);
	else
		glOrtho(-nRange * aspectRatio, nRange * aspectRatio, -nRange, nRange, nRange, -nRange);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(400, 400);
	glutCreateWindow("simple");

	SetupRC();
	glutDisplayFunc(RenderScene);
	glutReshapeFunc(ChangeSize);
	glutKeyboardFunc(keyboard);
	glutSpecialFunc(SpecialKeys);
	glutMainLoop();
}
