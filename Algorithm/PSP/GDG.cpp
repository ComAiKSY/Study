#include <iostream> // 전처리 지시문 (표준 입출력)
using namespace std; // std:: 없이 cout, cin 등을 직접 쓰게 해줌

int main(){ // 두 양의 정수가 주어졌을 때 최대 공약수 구해라 (재귀함수 미사용)

    int num1, num2, min; // num1, num2 : 입력받을 두 양의 정수, min : 최솟값 찾기
    int gdg=1; // 최대공약수

    cout << "두 정수를 입력 : " ;
    cin >> num1 >> num2;
    
    if(num1 < num2){ // 두 정수중 최솟값 찾기
        min = num1;
    }
    else min = num2;

    //GDG(num1, num2, min);
    
    for(int i=2; i<=min; i++){ // 2 ~ min 만큼 나누기 실행
        while(num1%i==0 && num2%i==0){  // i를 나누어 나머지가 0이면 공약수

            gdg=gdg*i;
            num1 = num1/i;
            num2 = num2/i;

            cout <<"GDG :" << gdg << " num1 : " << num1 << " num2:" << num2 <<endl;
        }
    }

    cout << "최대 공약수 : " << gdg << endl;
}

// int GDG(int num1, int num2, int min){
//     for(int i=2; i<=min; i++){

//     }
// }