#include <GL/glut.h> // 원그리기 + 점 찍기
#include <stdio.h>
#include <iostream>
#include <cmath>;
#define GL_PI 3.1415f
// 정면 렌더링
//void RenderScene(void) {
//    //std::cout << "Render Scene" << std::endl;
//    float radius = 50.0f;
//    int num = 16;
//
//    float md1 = 0.0f, md2 = 0.0f; 
//
//    glBegin(GL_TRIANGLES);
//    for (int i = 0; i < num; i++) {
//        float angle1 = 2.0f * GL_PI * i / num;
//        float angle2 = 2.0f * GL_PI * (i + 1) / num;
//
//        float x1 = cos(angle1) * radius;
//        float y1 = sin(angle1) * radius;
//
//        float x2 = cos(angle2) * radius;
//        float y2 = sin(angle2) * radius;
//
//       
//        if (i % 2 == 0)
//            glColor3f(1.0f, 0.0f, 0.0f);  // 빨간색
//        else
//            glColor3f(0.0f, 1.0f, 0.0f);  // 초록색
//
//        glVertex2f(md1, md2);   // 중심점
//        glVertex2f(x1, y1);   // 외곽점 1
//        glVertex2f(x2, y2);   // 외곽점 2
//    }
//    glEnd();
//
//    glutSwapBuffers();
//}
void RenderScene(void) {
    //std::cout << "Render Scene" << std::endl;
    glColor3f(0.0f, 1.0f, 0.0f);  // 녹색
    int num= 16;
    float radius = 50.0f;

    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0.0f, 0.0f);  // 중심점

    for (int i = 0; i <= num; i++) {
        float angle = 2.0f * GL_PI * i / num;
        float x = cos(angle) * radius;
        float y = sin(angle) * radius;
        glVertex2f(x, y);
    }
    glEnd();

    glPointSize(10.0f);
    glBegin(GL_POINTS);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(0.0f, 0.0f);  // 중심점

    for (int i = 0; i <= num; i++) {
        float angle = 2.0f * GL_PI * i / num;
        float x = cos(angle) * radius;
        float y = sin(angle) * radius;
        glVertex2f(x, y);
    }
    glEnd();

    glutSwapBuffers();
}

void SetupRC(void) {
    std::cout << "SetupRC" << std::endl;
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glShadeModel(GL_SMOOTH);
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