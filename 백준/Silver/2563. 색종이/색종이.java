import java.util.Scanner;
public class Main{
      public static void main(String[] args) {
    int[][] arr = new int[100][100];
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int sum = 0;
    for (int i = 0; i < N; i++ ) {
      int x = scanner.nextInt();
      int y = scanner.nextInt();
      for (int j = x-1; j < x+9; j++) {
        for(int k = y-1; k < y+9; k++) {
          arr[j][k] = 1;
        }
      }
    }
    for(int i = 0; i < 100 ; i++) {
      for(int j = 0; j<100;j++) {
//        System.out.print(arr[i][j]);
        if(arr[i][j] == 1) {
          sum++;
        }

      }
//      System.out.println();
    }
    System.out.print(sum);
  }
    
}