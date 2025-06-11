#include <GL/glut.h>
#include <iostream.

#define GL_PI 3.1415f

bool bCull = 1;
int num = 0;

void keyboard(unsigned char key, int x, int y){
    if(key == '1')
        num = 0;
    else if (key == '2')
        num = 2;
    else if (key == '3')
        num = 3;
    else if (key == '4')
        num = 4;
    else if (key == '5')
        num = 5;
    else if (key == '6')
        num = 6;
    else if (key == '7')
        num = 7;
    else if (key == '8')
        num = 8;

    glutPostRedisplay();
}

void RenderScene(void){

    glClear(GL_COLOR_BUFFER_BIT);
    if(bCull)
        glEnable(GL_CULL_FACE);
    else
        glDisable(GL_CULL_FACE);

    glPushMatrix();
    GLfloat x, y, anle;
    int iPivot = 1;
    int count = 0;
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0.0f, 0.0f);

    for (angle=0.0fl angle < (2.05f * GL_PI); angle += (GL_PI/4.0f))
    {
        if(count == num+1)
            break;
        x=50.0f * cos(angle);
        y=50.0f * sin(angle);

        if((iPivot%2)==0)
            glColor3f(0.0f, 1.0f, 0.0f);
        else
            glColor3f(1.0f,0.0f,0.0f);
        
        iPivot++;
        count++;
        glVertex2f(x,y);
    }
    glEnd();

    glPopMatrix();
    glSwapBuffer();
}

void SetupRC(void)
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glShowModel(GL_FLAT);
}

void ChangeSize(GLsizei w, GLsizei h) {
	// std::cout << "w = " << w << " " << " h = " << h << std::endl;
	// std::cout << "ChangeSize" << std::endl;

	GLint nRange = 100.0f;
	GLfloat aspectRatio;
	if (h == 0) {
		h = 1;
	}
	glViewport(0, 0, w, h);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	aspectRatio = (GLfloat)w / (GLfloat)h;
	if (w <= h)
		glOrtho(-nRange, nRange, -nRange / aspectRatio, nRange / aspectRatio, nRange, -nRange);
	else
		glOrtho(-nRange * aspectRatio, nRange * aspectRatio, -nRange, nRange, nRange, -nRange);

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
	glutKeyboardFunc(keyboard);
	glutMainLoop();
}