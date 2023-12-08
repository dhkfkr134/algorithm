/* https://www.acmicpc.net/problem/2444
 * 
 */


package deepening1;

import java.util.Scanner;
public class Ex03 {
  
  public static void main(String[] args) {
    int N = new Scanner(System.in).nextInt();
    for (int i = -N+1; i < N; i++) {
      int x = Math.abs(i);
      for(int j = 0; j < x; j++) {
        System.out.print(' ');
      }
      int y = (N-x)*2-1;
      for(int k = 0; k < y; k++ ) {
        System.out.print('*');
      }

      System.out.println();
    }
  }
}
