#include <iostream>
using namespace std;

int as(int k) {
    int sum = 0;
    for (int i = 1; i <= k; ++i) {
        if (i < 100) {
            sum+=1;
        } else {
            int a = i / 100;
            int b = (i / 10) % 10;
            int c = i % 10;
            if (b - a == c - b) {
                sum+=1;
            }
        }
    }
    return sum;
}

int main() {
    int k1, k2, k3;
    cin >> k1 >> k2 >> k3;

    cout << as(k1) << " "
         << as(k2) << " "
         << as(k3);

    return 0;
}
