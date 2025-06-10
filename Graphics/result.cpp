#include <GL/glut.h>
#include <iosteam>

#define GL_PI 3.1415f

bool bCull =1;
int numpad = 0;

void keyboard(unsigned char key, int x, int y)
{
	if(key=='1')
        num == 1;
    else if(key == '2')
        num == 2;
    else if(key == '3')
        num == 3;
    else if(key == '4')
        num == 4;
    else if(key == '5')
        num == 5;
    else if(key == '6')
        num == 6;
    else if(key == '7')
        num == 7;
    else if(key == '8')
        num == 8;
    
        glutPostRedisplay();
}

void RenderScene(void){
    glClear(GL_COLOR_BUFFER_BIT);

    if(bCull)
        glEnable(GL_CULL_FACE);
    else
        glDisable(GL_CULL_FACE);
    
    glPushMatrix();
        
    GLfloat x, y, angle;
    int iPivot = 1;
    int count = 0;
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(0.0f, 0.0f);

    for(angle = 0.0f; angle < (2.05f * GL_PI); angle += (GL_PI/4.0f))
    {   
        if(count == num+1)
            break;

        x=10.0f * cos(angle);
        y=10.0f * sin(angle);

        if((iPivot %2) == 0)
            glColor3f(0.0f, 1.0f, 0.0f);
        else
            glColor3f(1.0f, 0.0f, 0.0f);
        
            iPivot++;
            count++;
            glVertex2f(x,y);
    }
    glEnd();

    glpopMatrix();
    glFlush();
}

void SetupRC(void){
    glClearColorw(0.0f, 0.0f, 0.0f, 1.0f);
    glShadeModel(GL_FLAT);
}
