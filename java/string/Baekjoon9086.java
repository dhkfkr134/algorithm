package string;

import java.util.Scanner;

public class Baekjoon9086 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int T = Integer.parseInt(scanner.nextLine());
    for(int i =0; i< T; i++) {
      String S = scanner.nextLine();
      System.out.printf("%c%c\n",S.charAt(0),S.charAt(S.length()-1));
    }
    }
}