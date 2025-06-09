#include <GL/glut.h>
#include <iostream>
#include <cmath>

#define GL_PI 3.1415f

int count = 0;  // 보여줄 조각 수 (1~8)

void RenderScene(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    int num = 8;
    float radius = 50.0f;

    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0.0f, 0.0f);  // 중심점

    for (int i = 0; i <= count; i++) {
        float angle = 2.0f * GL_PI * i / num;
        float x = cos(angle) * radius;
        float y = sin(angle) * radius;

        if (i % 2 == 0)
            glColor3f(0.0f, 1.0f, 0.0f);  // 초록
        else
            glColor3f(1.0f, 0.0f, 0.0f);  // 빨강

        glVertex2f(x, y);
    }

    glEnd();

    glutSwapBuffers();
    glFlush();
}

void keyboard(unsigned char key, int x, int y) {
    if (key >= '1' && key <= '8') {
        count = key - '0';        // '1' → 1, ..., '8' → 8
        glutPostRedisplay();      // 다시 그리기 요청
    }
}

void SetupRC(void) {
    std::cout << "SetupRC" << std::endl;
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glShadeModel(GL_FLAT);
}

void ChangeSize(GLsizei w, GLsizei h) {
    std::cout << "w = " << w << " " << " h = " << h << std::endl;

    GLfloat aspectRatio;

    if (h == 0) h = 1;
    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    aspectRatio = (GLfloat)w / (GLfloat)h;
    if (w <= h)
        glOrtho(-100, 100, -100 / aspectRatio, 100 / aspectRatio, -500, 500);
    else
        glOrtho(-100 * aspectRatio, 100 * aspectRatio, -100, 100, -500, 500);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(400, 400);
    glutCreateWindow("Redner");  // 창 제목 고정

    SetupRC();
    glutDisplayFunc(RenderScene);
    glutReshapeFunc(ChangeSize);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}
