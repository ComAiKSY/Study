#include <GL/glut.h>
#include <iostream>

void DrawArrow(float x, float y, float z, float dx, float dy, float dz, float arrowSize) {
    // 선 부분
    glBegin(GL_LINES);
    glVertex3f(x, y, z);
    glVertex3f(x + dx, y + dy, z + dz);
    glEnd();

    // 삼각형 (화살촉)
    float endX = x + dx;
    float endY = y + dy;
    float endZ = z + dz;

    glBegin(GL_TRIANGLES);
    if (dx != 0) {
        glVertex3f(endX, endY + arrowSize, endZ);
        glVertex3f(endX, endY - arrowSize, endZ);
        glVertex3f(endX + arrowSize * 1.5f, endY, endZ);
    }
    else if (dy != 0) {
        glVertex3f(endX + arrowSize, endY, endZ);
        glVertex3f(endX - arrowSize, endY, endZ);
        glVertex3f(endX, endY + arrowSize * 1.5f, endZ);
    }
    else if (dz != 0) {
        glVertex3f(endX, endY + arrowSize, endZ);
        glVertex3f(endX, endY - arrowSize, endZ);
        glVertex3f(endX, endY, endZ + arrowSize * 1.5f);
    }
    glEnd();
}

void RenderScene(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-300, 300, -300, 300, -300, 300);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    // 카메라 각도 회전 → 실행 시 바로 보이게
    glRotatef(30, 1, 1, 0);  // X+Y 방향 회전

    // 점선 축
    glEnable(GL_LINE_STIPPLE);
    glLineStipple(1, 0x00FF);
    glLineWidth(2.0f);

    float len = 150.0f;
    float arrowSize = 6.0f;

    // X축 - 빨강
    glColor3f(1.0f, 0.0f, 0.0f);
    DrawArrow(0, 0, 0, len, 0, 0, arrowSize);

    // Y축 - 초록
    glColor3f(0.0f, 1.0f, 0.0f);
    DrawArrow(0, 0, 0, 0, len, 0, arrowSize);

    // Z축 - 파랑
    glColor3f(0.0f, 0.0f, 1.0f);
    DrawArrow(0, 0, 0, 0, 0, len, arrowSize);

    glDisable(GL_LINE_STIPPLE);

    glutSwapBuffers();
    glFlush();
}

void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // 배경: 검정
    glEnable(GL_DEPTH_TEST);              // 깊이 버퍼 활성화
    glFrontFace(GL_CCW);                  // 와인딩: 반시계 방향을 앞면
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(400, 300);
    glutCreateWindow("Render");
    SetupRC();
    glutDisplayFunc(RenderScene);
    glutMainLoop();
}
