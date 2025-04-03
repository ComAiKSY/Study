#include <GL/glut.h>
#include <stdio.h>
#include <iostream>
#include <cmath>;
#define GL_PI 3.1415f
// 원 만들기
// 정면 렌더링
void RenderScene(void) {
    std::cout << "Render Scene" << std::endl;

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 0.0f, 0.0f);
    glPointSize(1.0);
    glBegin(GL_POINTS);
    for (float i = 0.0f; i <= 2.0f * (GL_PI); i += 0.1f) {
        float x = cos(i) * 50;
        float y = sin(i) * 50;
        glVertex2f(x, y);
    }
    glEnd();


    glutSwapBuffers();
}

void SetupRC(void) {
    std::cout << "SetupRC" << std::endl;
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
}

void ChangeSize(GLsizei w, GLsizei h) {
    std::cout << "w = " << w << " " << " h = " << h << std::endl;
    std::cout << "ChangeSize" << std::endl;

    GLint wSize = 1;
    GLfloat aspectRatio;

    if (h == 0) {
        h = 1;
    }
    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // 여기에 작성
    aspectRatio = (GLfloat)w / (GLfloat)h;
    if (w <= h)
        glOrtho(-100, 100, -100 / aspectRatio, 100 / aspectRatio, -50, 50); // 세로가 더 기니까 세로를 늘려서 사각형의 비율을 유지
    else
        glOrtho(-100 * aspectRatio, 100 * aspectRatio, -100, 100, -50, 50); // 가로가 더 기니까 가로 보는 시야를 늘려서? 사각형의 비율을 유지
    // 여기에 작성
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
    glutMainLoop();
}