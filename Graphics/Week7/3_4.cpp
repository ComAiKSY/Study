#include <GL/glut.h>
#include <iostream>
#include <cmath>
#define GL_PI 3.1415f  // 원주율 정의

// 화면에 그릴 내용 정의
void RenderScene(void) {
    std::cout << "Render Scene" << std::endl;

    // 화면 초기화 (배경색으로)
    glClear(GL_COLOR_BUFFER_BIT);

    // 선 색상 설정 (빨간색)
    glColor3f(1.0f, 0.0f, 0.0f);

    // 모델뷰 행렬 저장
    glPushMatrix();

    // 시점 회전: x축으로 45도, y축으로 45도 회전
    glRotatef(45, 1.0f, 0.0f, 0.0f);
    glRotatef(45, 0.0f, 1.0f, 0.0f);

    // 선 그리기 시작: 점들을 선으로 연결 (끊기지 않음)
    glBegin(GL_LINE_STRIP);

    float z = -45.0f;  // z축 위치 초기값
    for (float i = 0.0f; i <= 6.0f * GL_PI; i += 0.1f) {
        // 나선형 위치 계산
        float x = cos(i) * 50;
        float y = sin(i) * 50;

        // 계산한 좌표를 정점으로 추가
        glVertex3f(x, y, z);

        // z축으로 점점 앞으로 이동
        z += 0.3f;
    }

    // 선 그리기 종료
    glEnd();

    // 이전 행렬 복원
    glPopMatrix();

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
