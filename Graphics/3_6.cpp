#include <GL/glut.h>
#include <iostream>

void RenderScene(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-200, 200, -200, 200, -1, 1);  // 2D 좌표계

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    // 빨간색 사각형
    glColor3f(1.0f, 0.0f, 0.0f);

    float x1 = 0, y1 = 0;
    float x2 = 100, y2 = 100;

    glBegin(GL_TRIANGLE_STRIP);
    glVertex2f(x1, y1);  // 아래 왼쪽
    glVertex2f(x1, y2);  // 위 왼쪽
    glVertex2f(x2, y1);  // 아래 오른쪽
    glVertex2f(x2, y2);  // 위 오른쪽
    glEnd();

    glutSwapBuffers();
    glFlush();
}

void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // 배경: 검정
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(400, 300);
    glutCreateWindow("Redner");

    SetupRC();
    glutDisplayFunc(RenderScene);
    glutMainLoop();
}
