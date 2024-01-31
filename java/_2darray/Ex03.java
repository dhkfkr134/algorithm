/*
 * https://www.acmicpc.net/problem/10798
 * 
 */
package _2darray;

import java.util.Scanner;

public class Ex03 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    char[][] arr = new char[5][15];
    for (int i = 0; i < 5; i++) {
      String str = scanner.nextLine();
      for(int j = 0; j < str.length() ; j++) {
      arr[i][j] = str.charAt(j);
      }
     }
    for (int j = 0; j < arr[0].length; j++) {
      for (int k = 0; k < 5; k++) {
        if(arr[k][j] != 0)
        System.out.print(arr[k][j]);
      }
    }
  }
}
