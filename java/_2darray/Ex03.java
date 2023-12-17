/*
 * https://www.acmicpc.net/problem/10798
 * 
 */
package _2darray;

import java.util.Scanner;

public class Ex03 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String[] arr = new String[5];
    char[][] trr = new char[15][5];
    for (int i = 0; i < 5; i++) {
      arr[i] = scanner.nextLine();
      }
    for (int j = 0; j < arr[0].lenght(); j++) {
      for (int k = 0; k < 5; k++) {
        System.out.print(arr[k][j]);
      }
    }
    for(int i = 0; i < 5 ; i++) {
      for (int j =0 ; j < trr[i].length; j++) {
        System.out.printf("%c ", trr[i][j]);
      }
      System.out.println("");
    }
  }
}
