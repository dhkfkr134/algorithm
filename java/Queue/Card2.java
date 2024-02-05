package Queue;

import java.util.LinkedList;
import java.util.Scanner;

public class Card2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    LinkedList<Integer> q = new LinkedList<>();
    Integer N = sc.nextInt();
    for (int i = 1; i< N+1; i++) {
      q.add(i);
    }
    while (q.size() > 1) {
    q.pollFirst();
    q.addLast(q.pollFirst());
    }
    System.out.println(q.get(0));
    
  }
}
