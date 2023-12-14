/*
 * https://www.acmicpc.net/problem/2738
 * 
 */
package _2darray;

import java.util.Scanner;

public class Ex02 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int max = 0;
    int row = 1;
    int col = 1;
    for (int x = 0; x< 9; x++) {
      for (int y = 0; y< 9; y++) {
        int temp = scanner.nextInt();
        if (temp >= max) {
          max = temp;
          row = x+1;
          col = y+1;
        }
      }
    }
    System.out.printf("%d\n%d %d",max,row,col);
  }
}
