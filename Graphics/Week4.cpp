#include <GL/glut.h>
#include <iostream>
using namespace std;

void RenderScene(void){ // 화면 조정시 사각형 비율 자동 조정
    cout << "RenderScene" << endl;

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 0.0f, 0.0f);
    glRectf(-0.25f, 0.25f, 0.25f, -0.25f); // -0.25~0.25 정규화 좌표 (비율 유지됨)

    glFlush();
}

void SetupRC(void){
    cout << "SetupRC" << endl;
    glClearColor(0.0f, 0.0f, 1.0f, 1.0f); // 배경 파란색
}

void ChangeSize(GLsizei w, GLsizei h){
    GLfloat aspectRatio;

    if(h == 0) h = 1; // 0으로 나누기 방지

    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    aspectRatio = (GLfloat)w / (GLfloat)h; // 비율 설정

    // plus: 비율 유지하는 glOrtho
    if (w <= h)
        glOrtho(-1.0, 1.0, -1.0 / aspectRatio, 1.0 / aspectRatio, -1.0, 1.0);
    else
        glOrtho(-1.0 * aspectRatio, 1.0 * aspectRatio, -1.0, 1.0, -1.0, 1.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char **argv){
    glutInit(&argc, argv); 
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(400, 400); 
    glutCreateWindow("simple");

    SetupRC();

    glutDisplayFunc(RenderScene);
    glutReshapeFunc(ChangeSize); // 창 크기 수정할 때 콜백함수

    glutMainLoop();
}