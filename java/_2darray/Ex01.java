/*
 * https://www.acmicpc.net/problem/2738
 * 2차원배열은 왠만해서는 이중for문아닌가?
 */
package _2darray;

import java.util.Scanner;

public class Ex01 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int x = scanner.nextInt();
    int y = scanner.nextInt();
    int[][] array = new int[x][y];
    int[][] array2 = new int[x][y];
    for (int i = 0; i < x; i++) {
      for (int j = 0; j < y; j++) {
        array[i][j] = scanner.nextInt();
      }
    }
    for (int i = 0; i < x; i++) {
      for (int j = 0; j < y; j++) {
        array2[i][j] = scanner.nextInt() + array[i][j];
        System.out.printf("%d ",array2[i][j]);
      }
      System.out.println();
    }
    
  }
}
