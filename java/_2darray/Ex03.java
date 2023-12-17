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
    for (int j = 0; j < 5; j++) {
      for (int k = 0; k < arr[j].length(); k++) {
        System.out.printf("%d, %d, %d\n",j,k,arr[j].length());
        trr[k][j] = arr[j].charAt(k);
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
