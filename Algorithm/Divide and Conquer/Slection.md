# 정의
- #### 전체 n개의 숫자들 중에서 k 번째로 작은 숫자를 찾는 문제 (최댓값 찾기와 유사)

# 단순한 알고리즘
- #### 최소 숫자를 k번 찾음
- #### 숫자들을 정렬한 후, k번째 숫자 찾음

# 아이디어
    # 이진 탐색
    - #### 정렬된 입력의 중간에 있는 숫자와 찾고자 하는 숫자를 비교

    # 선택 문제
    - #### pivot을 선택하여 분할

# sudo code
    Selection(A, left, right, k) //k:그룹내에서 몇번째
    input: A[left]~A[right]와 k, 단, 1≤k≤|A|, |A|=right-left+1
    output: A[left]~A[right]에서 k번째 작은 원소
    1. pivot을 A[left]~A[right]에서 랜덤하게 선택하고, pivot과 A[left]의 자리를 바꾼 후, pivot과 배
    열의 각 원소를 비교하여 pivot 보다 작은 숫자는 A[left]~A[p-1]로 옮기고, pivot 보다 큰 숫자
    는 A[p+1]~A[right]로 옮기며, pivot은 A[p]에 놓음
    2. S = (p-1)-left+1                  
    // S = Small group의 크기
    3. If (k ≤ S) Selection(A, left, p-1, k)    
    4. else if (k = S + 1) return A[p]         
    // Small group에서 찾기
    // pivot = k번째 작은 숫자
    5. else Selection(A, p+1, right, k-S-1)   // Large group에서 찾기

# 예제 (C)
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    // swap 함수
    void swap(int *a, int *b) {
        int temp = *a;
        *a = *b;
        *b = temp;
    }

    // Selection를 위한 분할 함수
    int partition(int arr[], int left, int right, int pivotIndex) {
        int pivotValue = arr[pivotIndex];
        swap(&arr[pivotIndex], &arr[right]);  // pivot 배열 끝 이동
        int storeIndex = left;
        
        for (int i = left; i < right; i++) {
            if (arr[i] < pivotValue) {
                swap(&arr[storeIndex], &arr[i]);
                storeIndex++;
            }
        }
        swap(&arr[right], &arr[storeIndex]);  // 피벗을 최종 위치로 이동
        return storeIndex;
    }

    // Selection 알고리즘
    int Selection(int arr[], int left, int right, int k) {
        if (left == right) {
            return arr[left]; // 배열에 하나의 요소만 있을 경우
        }
        
        int pivotIndex = left + (rand() % (right - left + 1));  // 랜덤 pivot 선택
        pivotIndex = partition(arr, left, right, pivotIndex);
        
        if (k == pivotIndex) {
            return arr[k];  // pivot이 k번째 요소일 경우
        } else if (k < pivotIndex) {
            return Selection(arr, left, pivotIndex - 1, k);
        } else {    
            return Selection(arr, pivotIndex + 1, right, k);
        }
    }

    // 입력파일 읽기
    int readFile(const char* filename, int arr[], int maxSize) {
        FILE* file = fopen(filename, "r");
        if (!file) {
            printf("fopen error.\n");
            return -1;
        }
        
        int i = 0;
        while (fscanf(file, "%d", &arr[i]) != EOF && i < maxSize) {
            i++;
        }
        
        fclose(file);
        return i;  // 읽은 요소 개수 반환
    }

    int main() {
        const char* filename = "inupt_sort.txt";
        int arr[1000];
        
        // 파일 읽기
        int size = readFile(filename, arr, 1000);
        if (size == -1) {
            return -1;
        }
        
        // 시작 시간 측정
        clock_t start = clock();
        
        // 50번, 70번 찾기
        int element50 = Selection(arr, 0, size - 1, 49);
        int element70 = Selection(arr, 0, size - 1, 69);
        
        // 종료 시간 측정
        clock_t end = clock();
        double time_spent = (double)(end - start) / CLOCKS_PER_SEC;
        
        // 결과 출력
        printf("50 num: %d\n", element50);
        printf("70 num: %d\n", element70);
        printf("Selection Running time : %f s\n", time_spent);
        
        return 0;
    }
