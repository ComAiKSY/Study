#include <stdio.h>
#include <iostream>
#include <GL/glut.h>
#include <math.h>

#define GL_PI 3.1415f

int iPivot = 1;
bool bCull = true;
bool bDepth = true;
GLfloat xRot = 0.0f, yRot = 0.0f;
GLfloat xTran = 0.0f, yTran = 0.0f;

void SpecialKeys(int key, int x, int y) {
	if (key == GLUT_KEY_UP) xRot -= 2.0f;
	if (key == GLUT_KEY_DOWN) xRot += 2.0f;
	if (key == GLUT_KEY_LEFT) yRot -= 2.0f;
	if (key == GLUT_KEY_RIGHT) yRot += 2.0f;

	if (xRot > 360.0f) xRot -= 360.0f;
	if (xRot < 0.0f) xRot += 360.0f;
	if (yRot > 360.0f) yRot -= 360.0f;
	if (yRot < 0.0f) yRot += 360.0f;

	glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y) {
	if (key == 'a') xTran -= 2.0f;
	else if (key == 'd') xTran += 2.0f;
	else if (key == 'w') yTran += 2.0f;
	else if (key == 's') yTran -= 2.0f;
	glutPostRedisplay();
}

// 장면 랜더링
void RenderScene(void) {
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glLoadIdentity(); // 변환 행렬 초기화

	glPushMatrix(); // 현재 행렬 상태 저장

	glTranslatef(0.0f, 0.0f, -30.0f); // 카메라를 뒤로 이동
	glRotatef(30.0f, 1.0f, 0.0f, 0.0f); // X축 회전
	glRotatef(-30.0f, 0.0f, 1.0f, 0.0f); // Y축 회전

	glBegin(GL_LINES);
	// X축 (빨간색)
	glColor3f(1.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(50.0f, 0.0f, 0.0f);

	// Y축 (초록색)
	glColor3f(0.0f, 1.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 50.0f, 0.0f);


	glColor3f(0.0f, 0.0f, 1.0f);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 50.0f);
	glEnd();


	glEnable(GL_LINE_STIPPLE);                 
	glLineStipple(1, 0x0F0F);                  
	glColor3f(0.0f, 0.0f, 1.0f);                
	glutWireCube(10.0f);                       
	glDisable(GL_LINE_STIPPLE);

	glPushMatrix(); 
	glTranslatef(0.0f, 15.0f, 0.0f); 
	glColor3f(1.0f, 0.0f, 0.0f); 
	glutWireCube(10.0f);

	glPopMatrix(); 

	
	glutSwapBuffers(); 
}


void SetupRC(void) {
	std::cout << "SetupRC" << std::endl;
	glClearColor(1.0f, 1.0f, 1.0f, 0.0f);
	glEnable(GL_POINT_SMOOTH);       // 점을 부드럽게 (원처럼) 보이게
	glHint(GL_POINT_SMOOTH_HINT, GL_NICEST); // 스무딩 힌트: 최고 품질
	glShadeModel(GL_FLAT);
}

void ChangeSize(GLsizei w, GLsizei h) {
	std::cout << "w = " << w << " " << "h = " << h << std::endl;
	std::cout << "ChangeSize" << std::endl;

	GLint wSize = 100;
	GLfloat aspectRatio;

	if (h == 0)
		h = 1;

	glViewport(0, 0, w, h);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	aspectRatio = (GLfloat)w / (GLfloat)h;
	if (w <= h)
		glOrtho(-wSize, wSize, -wSize / aspectRatio, wSize / aspectRatio, -wSize, wSize);
	else
		glOrtho(-wSize * aspectRatio, wSize * aspectRatio, -wSize, wSize, -wSize, wSize);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	//glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("simple");

	SetupRC();
	glutDisplayFunc(RenderScene);
	glutReshapeFunc(ChangeSize);
	glutKeyboardFunc(keyboard);
	glutSpecialFunc(SpecialKeys);
	glutMainLoop();
}