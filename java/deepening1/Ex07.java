/*
 * https://www.acmicpc.net/problem/1316
 * String.contain() , String.substring()
 * 메서드를 알면 문제 그대로 접근할 수 있다.
 */

package deepening1;

import java.util.Scanner;
public class Ex07 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = Integer.parseInt(scanner.nextLine());
    String word ="";
    int answer = N;
    for (int i = 0; i < N; i++) {
      word = scanner.nextLine();
       for(int j = 0; j < word.length()-1; j++) {

         if(word.charAt(j) == word.charAt(j+1)) {
           ;
         }

         else if(word.substring(j+1).contains(""+word.charAt(j))) {
           answer --;
           break;
         }
       }
       
    }
    System.out.print(answer);
  }
  
}
