# 정의
- #### 입력 2개인 부분 문제로 분할
- #### 부분 문제의 크기가 1/2로 감소하는 알고리즘
- #### 합병 과정이 문제를 정복하는 과정

# 시간 복잡도
- #### 최악의 경우에 대한 시간 복잡도 O(nlogn)

# sudo code
    MergeSort(A,p,q) A:입력, p:Subgroup first index, q:Subgroup last index
    Input:A[p] ~ A[q]
    Output:정렬된 A[p] ~ A[q]

    if(p<q){                // 배열의 원소의 수가 2개 이상이면
        k=floor((p+q)/2)    // k는 중간 원소의 index floor(a):a보다 작은 가장 큰 정수
        MergeSort(A,p,k)    // 앞부분 순환 호출
        MergeSort(A,k+1,q)  // 뒷부분 순환 호출
        A[p]~A[k]와 A[k+1]~A[q]를 합병
    } 

# 예제 (C++)
```
#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

// 두 서브 배열을 병합하는 함수
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // 임시 배열
    vector<int> leftArr(n1), rightArr(n2);

    // 데이터를 임시 배열에 복사
    for (int i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        rightArr[i] = arr[mid + 1 + i];

    // 임시 배열을 원래 배열에 병합
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    // 남은 leftArr 요소 복사
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    // 남은 rightArr 요소 복사
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// 병합 정렬 함수
void mergeSort(vector<int>& arr, int left, int right) {
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

int main() {
    // 입력 파일 열기
    ifstream inputFile("inupt_sort.txt");
    if (!inputFile) {
        cerr << "input error" << endl;
        return 1;
    }

    // 숫자 읽기
    vector<int> numbers;
    int num;
    while (inputFile >> num) {
        numbers.push_back(num);
    }
    inputFile.close();

    // 시작 시간 측정
    auto start = high_resolution_clock::now();

    // 병합 정렬 호출
    mergeSort(numbers, 0, numbers.size() - 1);

    // 종료 시간 측정
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);

    // 정렬된 숫자를 출력 파일에 쓰기
    ofstream outputFile("output_merge_sort.txt");
    if (!outputFile) {
        cerr << "output error" << endl;
        return 1;
    }

    for (int n : numbers) {
        outputFile << n << endl;
    }
    outputFile.close();

    // 실행 시간 출력
    cout << "Merge sort Running time : " << duration.count() << " ms." << endl;

    return 0;
}
```
