import java.util.*;

class Main {
    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        int[] scanNum = new int[28]; // 학생 수에 맞게 배열 크기 조정
        int[] printNum = new int[31]; // 학생 번호에 맞게 배열 크기 조정

        for (int i = 0; i < 28; i++) { // 제출한 학생 수에 맞게 반복 횟수 조정
            scanNum[i] = sc.nextInt();
            printNum[scanNum[i]] = 1; // 제출한 학생 번호를 체크함
        }

        for (int i = 1; i <=30; i++) { // 학생 번호에 맞게 범위 설정
	        if (printNum[i] == 0) System.out.println(i); // 제출하지 않은 학생 출력
        }
    }
}
