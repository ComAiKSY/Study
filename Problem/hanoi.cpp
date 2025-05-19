#include <iostream>
using namespace std;

void H(int n, char A, char B, char C) //A : Start, B: Mid, C: End
{
    if (n == 1){
        cout << A << "->" << C << endl;
        return;
    }
    else
    {
        H(n-1, A, C, B);
        cout << A << "->" << C << endl;
        H(n-1, B, A, C);
    }
}

int main() {
    int N;
    cin >> N;
    cout << (1 << N) -1 << endl;
    H(N, 'A', 'B', 'C');
    return 0;
}