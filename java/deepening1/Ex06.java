/*
 * https://www.acmicpc.net/problem/2941
 * 직관적인 풀이(조건문처리)
 * else는 무조건 쓰자 이거떄매 개오래걸림
 */
package deepening1;

import java.util.Scanner;
public class Ex06 {
public static void main(String[] args) {
    
    String string = new Scanner(System.in).nextLine();
    int result = 0;
    
    for (int i = 0; i < string.length(); i++) {
      
      if (string.charAt(i) == 'c') {
        if(i < string.length() -1) {
          if(string.charAt(i+1) == '=') {
            i++;
          }
          else if(string.charAt(i+1) == '-') {
            i++;
          }
        }
      }
      
      else if (string.charAt(i) == 'd') {
        if(i < string.length() -1){ 
          if(string.charAt(i+1) == 'z') {
            if(i < string.length() - 2) {
              if(string.charAt(i+2) == '=') {
                i+=2;
              }
            }
          }
          else if(string.charAt(i+1) == '-') {
            i++;
          }
        }
      }
      
      else if (string.charAt(i) == 'l') {
        if(i < string.length() -1) {
          if(string.charAt(i+1) == 'j') {
            i++;
          }
        }
      }
      
      else if (string.charAt(i) == 'n') {
        if(i < string.length() -1) {
          if(string.charAt(i+1) == 'j') {
            i++;
          }
        }
      }

      
      else if (string.charAt(i) == 's') {
        if(i < string.length() -1) {
          if(string.charAt(i+1) == '=') {
            i++;
          }
        }
      }
      
      else if (string.charAt(i) == 'z' ) {
        if(i < string.length() -1) {
          if(string.charAt(i+1) == '=') {
            i++;
          }
        }
      }
      

      

      result++;
            
            
 
    }
    System.out.print(result);
  }
}
