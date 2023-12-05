/*
 * https://www.acmicpc.net/problem/10811
 *
 *
 *
 *
 */
package array;
import java.util.Scanner;

public class Baekjoon10811 {
  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt();
    int M = scanner.nextInt();
    
    int[] basket = new int[N];
    
    for(int i = 0; i<N; i++) {
      basket[i] = i+1;
    }
    
    for(int j =0; j< M; j++) {
      
      int x = scanner.nextInt();
      
      int y = scanner.nextInt();
      
      for(int l = x-1 ; l <(x+y)/2;l++) {
       
          int temp = basket[l];
          basket[l] = basket[x+y-l-2];
          basket[x+y-l-2] = temp;
        
      }
    }
    
    for(int k = 0; k < N; k++) {
      System.out.printf("%d ",basket[k]);
    }
  }
}
