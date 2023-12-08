/* https://www.acmicpc.net/problem/10988
 * 
 */
package deepening1;

import java.util.Scanner;
public class Ex04 {
  public static void main(String[] args) {
     String string = new Scanner(System.in).nextLine();
     int check = 1;
     int len = string.length();
     for (int i = 0; i < len; i++) {
       if(string.charAt(i) != string.charAt(len-1-i)) {
         check = 0;
         break;
       }
     }
     System.out.print(check);
  }
}
