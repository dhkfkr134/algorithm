package Queue;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Dequeue {
  public static LinkedList<Integer> q = new LinkedList<>();
  public static void main(String[] args) throws Exception {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    StringBuilder sb = new StringBuilder();
    
    int N = Integer.parseInt(st.nextToken());
    int C, X;
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      C = Integer.parseInt(st.nextToken());
      switch (C) {
      case 1: 
        X = Integer.parseInt(st.nextToken());
        q.addFirst(X);
        break;
      case 2:
        X = Integer.parseInt(st.nextToken());
        q.addLast(X);
        break;
      case 3:
        sb.append(popFirst() + "\n");
        break;
      case 4:
        sb.append(popLast() + "\n");
        break;
      case 5:
        sb.append(q.size()+"\n");
        break;
      case 6:
        if(q.isEmpty()) sb.append("1\n");
        else sb.append("0\n");
        break;
      case 7:
        sb.append(peekFirst()+"\n");
        break;
      case 8:
        sb.append(peekLast()+"\n");
        break;
      }
    }
    System.out.println(sb.toString());
  }
  public static int popFirst() {
    if(q.isEmpty()) return -1;
    else return q.pollFirst();
  }
  public static int popLast() {
    if(q.isEmpty()) return -1;
    else return q.pollLast();
  }
  public static int peekFirst() {
    if(q.isEmpty()) return -1;
    else return q.getFirst();
  }
  public static int peekLast() {
    if(q.isEmpty()) return -1;
    else return q.getLast();
  }
}
