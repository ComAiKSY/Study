# 정의
- #### 입력 2개인 부분 문제로 분할
- #### Pivot을 선택(첫번째, 마지막, 중간 값 or 랜덤)
- #### Pivot 보다 작은 값들은 왼쪽, 큰 값들은 오른쪽에 배치

# sudo code
    QuickSort(A, left, right)
    입력: 배열 A[left]~A[right]
    출력: 정렬된 배열 A[left]~A[right]
    1. if (left < right) {
    2.  피봇을 A[left]~A[right]에서 선택하고, 피봇을 A[left]와 자리를 바꾼 후, 피봇과 
        배열의 각 원소를 비교하여 피봇보다 작은 숫자들은 A[left]~A[p-1]으로 옮기고, 
        피봇보다 큰 숫자들은 A[p+1]~A[right]으로 옮기며, 피봇은 A[p]에 놓는다.
    3. QuickSort(A, left, p-1) //Pivot보다 작은 그룹
    4. QuickSort(A, p+1, right) //Pivot보다 큰 그룹
    }

# 예제 (JAVA)
```
import java.io.*;
import java.util.*;

public class Quick{
    
    // 퀵 정렬 함수
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high); // 배열 분할
            quickSort(arr, low, pi - 1); // pivot 왼쪽 정렬
            quickSort(arr, pi + 1, high); // pivot 오른쪽 정렬
        }
    }

    // 분할 함수
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high]; // 마지막 요소를 pivot 설정
        int i = (low - 1); // 작은 요소를 찾기 위한 index
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                // arr[i]와 arr[j] 교환
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        // arr[i+1], arr[high] or pivot 교환
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return i + 1; // pivot 최종 위치 반환
    }

    public static void main(String[] args) {
        try {
            // 입력 파일 읽기
            File file = new File("inupt_sort.txt");
            BufferedReader br = new BufferedReader(new FileReader(file));

            List<Integer> list = new ArrayList<>();
            String line;
            while ((line = br.readLine()) != null) {
                list.add(Integer.parseInt(line)); // 숫자로 변환후 리스트에 추가
            }
            br.close();

            // 배열로 변환
            int[] arr = list.stream().mapToInt(i -> i).toArray();

            // 실행 시간 측정
            long startTime = System.nanoTime(); // 시작 시간 기록

            // 퀵 정렬 수행
            quickSort(arr, 0, arr.length - 1);

            long endTime = System.nanoTime(); // 종료 시간 기록
            long duration = (endTime - startTime); // 실행 시간 계산 
            System.out.println("Quick sort Running time : " + duration + " ns");

            // 출력 파일
            BufferedWriter bw = new BufferedWriter(new FileWriter("output_quick_sort.txt"));
            for (int num : arr) {
                bw.write(num + "\n"); // 정렬된 배열 파일에 쓰기
            }
            bw.close();

        } catch (IOException e) {
            e.printStackTrace(); // 예외 발생 시 오류 메시지 출력
        }
    }
}
```
