#include <GL/glut.h>
#include <stdio.h>
#include <iostream>
#include <cmath>;
#define GL_PI 3.1415f
// 시점 로테이트 + 시작점 색깔 변경 + 점 사이즈 증강
void RenderScene(void) {
    std::cout << "Render Scene" << std::endl;

    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0f, 0.0f, 0.0f);

    glPushMatrix();
    glRotatef(45, 1.0f, 0.0f, 0.0f);
    glRotatef(45, 0.0f, 1.0f, 0.0f);


    float point_size = 3;
    float z = 0.0f;
    for (float i = 0.0f; i <= 6.0f * (GL_PI); i += 0.1f) { // 시작점 색깔 변경
        point_size += 0.1;
        glPointSize(point_size);
        glBegin(GL_POINTS);
        if (z == 0.0f)
        {
            glColor3f(0.0f, 1.0f, 0.0f);
        }
        float x = cos(i) * 50;
        float y = sin(i) * 50;
        glVertex3f(x, y, z);
        glColor3f(1.0f, 0.0f, 0.0f);
        z += 0.3f;
        glEnd();
    }

    

    glPopMatrix();

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
        glOrtho(-100, 100, -100 / aspectRatio, 100 / aspectRatio, -500, 500); // 세로가 더 기니까 세로를 늘려서 사각형의 비율을 유지
    else
        glOrtho(-100 * aspectRatio, 100 * aspectRatio, -100, 100, -500, 500); // 가로가 더 기니까 가로 보는 시야를 늘려서? 사각형의 비율을 유지
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