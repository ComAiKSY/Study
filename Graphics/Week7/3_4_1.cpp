#include <GL/glut.h>
#include <iostream>
#include <cmath>
#define GL_PI 3.1415f  // 원주율 정의

// 화면에 그릴 내용 정의
void RenderScene(void)
{
    // std::cout << "RenderScene" << std::endl; // 디버그 출력 (선택)

    GLfloat x, y;
    GLfloat sizes[2];      // [0]: 최소 굵기, [1]: 최대 굵기
    GLfloat curSize = 0.0f; // 현재 선 굵기

    // 화면 지우기 (검정 배경)
    glClear(GL_COLOR_BUFFER_BIT);

    // 선 색상 지정 (빨간색)
    glColor3f(1.0f, 0.0f, 0.0f);

    glPushMatrix(); // 현재 행렬 저장

    // 시스템이 지원하는 선 굵기 범위를 가져옴
    glGetFloatv(GL_LINE_WIDTH_RANGE, sizes);
    curSize = sizes[0]; // 최소 굵기부터 시작

    // 여러 굵기의 선을 아래로 나열하면서 그림
    for (y = -90.0f; y <= 90.0f; y += 20.0f)
    {
        glLineWidth(curSize);           // 현재 굵기로 선 그리기
        glBegin(GL_LINES);              // 선 그리기 시작
        glVertex2f(-80.0f, y);      // 왼쪽 점
        glVertex2f(80.0f, y);       // 오른쪽 점
        glEnd();

        curSize += 1.0f; // 선 굵기를 점점 증가시킴
    }

    glPopMatrix(); // 행렬 복원
    glFlush();     // 즉시 그리기 명령 실행

    // 더블 버퍼링: 화면에 출력
    glutSwapBuffers();
}

// 초기 설정 함수 (배경색 등)
void SetupRC(void) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // 배경색: 검정
}

// 창 크기 변경 시 호출되는 함수
void ChangeSize(GLsizei w, GLsizei h) {
    if (h == 0) h = 1;  // 0으로 나누는 것 방지
    glViewport(0, 0, w, h);  // 뷰포트 설정

    glMatrixMode(GL_PROJECTION);  // 투영 행렬 모드로 전환
    glLoadIdentity();  // 초기화

    // 화면 비율에 따라 종횡비 유지
    GLfloat aspectRatio = (GLfloat)w / (GLfloat)h;
    if (w <= h)
        glOrtho(-100, 100, -100 / aspectRatio, 100 / aspectRatio, -500, 500);  // 세로 보정
    else
        glOrtho(-100 * aspectRatio, 100 * aspectRatio, -100, 100, -500, 500);  // 가로 보정

    glMatrixMode(GL_MODELVIEW);  // 다시 모델뷰 모드로 전환
    glLoadIdentity();  // 초기화
}

// 메인 함수
int main(int argc, char** argv) {
    glutInit(&argc, argv);  // GLUT 초기화
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);  // 더블 버퍼 + RGB 색상
    glutInitWindowSize(500, 500);  // 창 크기
    glutInitWindowPosition(400, 400);  // 창 위치
    glutCreateWindow("simple");  // 창 생성

    SetupRC();  // 초기 설정
    glutDisplayFunc(RenderScene);  // 화면 그리기 함수 등록
    glutReshapeFunc(ChangeSize);  // 창 크기 변경 처리 함수 등록

    glutMainLoop();  // 메인 루프 진입 (이벤트 처리 반복)
}
