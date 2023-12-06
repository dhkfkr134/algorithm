// String객체에서 split()사용가능
package string;

import java.util.Scanner;

public class Baekjoon2908 {
  public static void main(String[] args){
    
    Scanner scanner = new Scanner(System.in);
    String A = scanner.next();
    String B = scanner.next();
    int X;
    int Y;
    X = Integer.parseInt(""+A.charAt(2)+A.charAt(1)+A.charAt(0));
    Y = Integer.parseInt(""+B.charAt(2)+B.charAt(1)+B.charAt(0));
    if (X > Y) System.out.print(X);
    else System.out.print(Y);
   }
     
  }
 
