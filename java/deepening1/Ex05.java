/*
 * https://www.acmicpc.net/problem/1157
 * 배열 인덱스로 해싱(순서가 있는 데이터)
 */
package deepening1;

import java.util.Scanner;
public class Ex05 {
  public static void main(String[] args) {
     int[] arr = new int[26];
     for(int j = 0; j < 26; j++) {
       arr[j] = 0;
     }
     String string = new Scanner(System.in).nextLine();
     for (int i = 0; i< string.length(); i++) {
       if (string.charAt(i) > 90) {
         arr[string.charAt(i)-97] += 1;
       }
       else {
         arr[string.charAt(i)-65] += 1;
       }
     }
     int max = 0;
     int value = 0;
     boolean isSame = false;
     for(int k = 0; k < 26; k++) {
       if(arr[k] > max) {
         max = arr[k];
         value = k;
         isSame = false;
       }
       else if(arr[k] == max) isSame = true;
     }
     if (isSame) System.out.println("?");
     else System.out.println((char)(value+65));
  }
}
