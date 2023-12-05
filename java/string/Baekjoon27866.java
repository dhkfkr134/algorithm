package string;

import java.util.Scanner;

public class Baekjoon27866 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String S = scanner.nextLine();
    int i = scanner.nextInt();
    
    System.out.print(S.charAt(i-1));
    }
}
