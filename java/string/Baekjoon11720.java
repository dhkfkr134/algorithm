package string;

import java.util.Scanner;

public class Baekjoon11720 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = Integer.parseInt(scanner.nextLine());
    int sum = 0;
    String X = scanner.nextLine();
    for(int i =0; i<N;i++) {
      sum += X.charAt(i)-'0';
    }
    System.out.print((int)sum);
  }
  
}
