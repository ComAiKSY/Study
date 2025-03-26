#include <GL/glut.h>
#include <stdio.h>
#include <iostream>

//장면 렌더링
void RenderScene(void){
	std::cout << "Render Scence" << std::endl;
	//현재 색상을 사용하여 화면을 지운다
	glClear(GL_COLOR_BUFFER_BIT);
	//드로잉 명령을 전달한다

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity(); // 좌표계 초기화

	glViewport(0, 0, 640, 480);

	//glOrtho(-1, 1, -1, 1, 1, -1); // 직접투영
	glOrtho(1, -1, 1, -1, 1, -1); // 직접투영 좌 우 하 상

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity(); // 좌표계 초기화

	glColor3f(1.0f, 0.0f, 0.0f); // 드로잉 색상을 결정

	// glRectf(-0.25f, -0.25f, 0.25f, 0.25f); // 사각형 그려주는 함수 (왼쪽 위 x, y / 오른쪽 아래 x, y)
	glRectf(0, 240, 320, 0);

	glFlush(); //강제적으로 GUI를 내보낸다, 싱글버퍼일 경우
}


void SetupRC(void)
{
	std::cout << "SetupRC" << std::endl;
	glClearColor(0.0f, 0.0f, 1.0f, 1.0f); // R G B A
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); //
	glutInitWindowSize(640, 480); // pixel size, glViewport를 설정하지 않으면 기본설정이 된다.
	glutInitWindowPosition(500, 500);
	glutCreateWindow("simple");

	SetupRC();
	glutDisplayFunc(RenderScene); // 콜백함수 (마우스, 키보드 등)

	glutMainLoop();
}