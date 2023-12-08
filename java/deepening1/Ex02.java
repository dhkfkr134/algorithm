/*
 * https://www.acmicpc.net/problem/3003
 */
package deepening1;

import java.util.Scanner;

public class Ex02 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    for(int i = 0; i < 6; i++) {
      int x = scanner.nextInt();
      if (i < 2) System.out.printf("%d ",1 - x);
      else if (i < 5) System.out.printf("%d ",2 - x);
      else System.out.printf("%d ",8 - x);
    }
  }
}
