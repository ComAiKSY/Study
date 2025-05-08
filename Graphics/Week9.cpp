#include <GL/glut.h>
#include <iostream>

// 정육면체 만들기 보이지 않는 부분은 점선


void RenderScene(void) {
    std::cout << "RenderScene" << std::endl;

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    // 투영 설정
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-200, 200, -200, 200, 200, -200);

    // 모델뷰 설정
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glRotatef(-45, 1.0f, 0.0f, 0.0f);  // 위에서 아래로 기울이기
    glRotatef(45, 0.0f, 1.0f, 0.0f);  // 좌측에서 우측으로 보기

    // 정육면체 꼭짓점
    GLfloat v[16][3] = {
        {0.0, 0.0, 0.0}, // 0
        {90.0,0.0, 0.0}, // 1
        {0.0, 90.0, 0.0}, // 2
        {90.0, 90.0, 0.0}, // 3
        {0.0, 0.0,90.0}, // 4
        {90.0, 0.0, 90.0}, // 5
        {0.0, 90.0, 90.0}, // 6
        {90.0, 90.0, 90.0},  // 7

        {180.0, 0.0, 0.0}, //8
        {180.0, 0.0, 90.0}, // 9
        {180.0, 90.0, 0.0}, //10
        {180.0, 90.0, 90.0},//11

        {0.0, 180.0, 0.0},//12
        {90.0,180.0,0.0},//13
        {0.0, 180.0, 90.0},//14
        {90.0, 180.0, 90.0}//15

  
    };

    // 실선
    glColor3f(1.0f, 0.0f, 0.0f); 
    glLineWidth(2.0f);
    glBegin(GL_LINES);
    
    glVertex3fv(v[0]); glVertex3fv(v[2]);
    glVertex3fv(v[0]); glVertex3fv(v[1]);
    
    glVertex3fv(v[1]); glVertex3fv(v[5]); //아래 오른쪽 아래
    glVertex3fv(v[2]); glVertex3fv(v[6]);// 왼 위 위 가로

    //glVertex3fv(v[4]); glVertex3fv(v[5]); // 아래 오른쪽 위
    glVertex3fv(v[6]); glVertex3fv(v[7]); // 위 오른쪽 위
    //glVertex3fv(v[4]); glVertex3fv(v[6]); // 뒤 중앙 
    glVertex3fv(v[5]); glVertex3fv(v[7]);

    glVertex3fv(v[2]); glVertex3fv(v[3]);
    glVertex3fv(v[1]); glVertex3fv(v[3]);
    glVertex3fv(v[3]); glVertex3fv(v[7]);

    glVertex3fv(v[1]); glVertex3fv(v[8]);
    glVertex3fv(v[8]); glVertex3fv(v[9]);
    glVertex3fv(v[8]); glVertex3fv(v[10]);
    glVertex3fv(v[3]); glVertex3fv(v[10]);
    glVertex3fv(v[10]); glVertex3fv(v[11]);

    glEnd();

    glEnable(GL_LINE_STIPPLE);

    glLineStipple(1, 0x00FF); 
    glColor3f(1.0f, 0.0f, 0.0f); 
    glBegin(GL_LINES);

    glVertex3fv(v[4]); glVertex3fv(v[6]);
    glVertex3fv(v[4]); glVertex3fv(v[5]);
    glVertex3fv(v[0]); glVertex3fv(v[4]);
    /*glVertex3fv(v[2]); glVertex3fv(v[3]);
    glVertex3fv(v[1]); glVertex3fv(v[3]);
    glVertex3fv(v[3]); glVertex3fv(v[7]);*/

    glVertex3fv(v[5]); glVertex3fv(v[9]);
    glEnd();
    glDisable(GL_LINE_STIPPLE);

    glutSwapBuffers();
    glFlush();
}

void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  
    glEnable(GL_DEPTH_TEST);           
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500,500);
    glutInitWindowPosition(400, 300);
    glutCreateWindow("Cube with Hidden Lines");

    SetupRC();
    glutDisplayFunc(RenderScene);
    glutMainLoop();
}
