package Queue;

import java.util.LinkedList;
import java.util.Scanner;

public class Balloonpop {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    LinkedList<Integer> q = new LinkedList<>();
    
    int N = sc.nextInt();
    int[] index = new int[1001];

    for (int i =0; i< N; i++) {
      index[i] = sc.nextInt();
      q.add(i+1);
    }
    sc.close();
    
    int pos = 0;
    for (int i = 0; i < N; i++) {
      int tmp = q.remove(pos);
      System.out.printf("%d ",tmp);
      if (q.isEmpty()) break;
      if (index[tmp-1] >= 0) pos = (pos + index[tmp-1]-1) % q.size();
      else if(index[tmp-1] + pos <0) pos = ((pos + index[tmp-1])%q.size()) +q.size();
      else pos = (pos + index[tmp-1])%q.size();
    }
  }
}
