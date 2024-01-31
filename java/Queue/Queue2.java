package Queue;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Queue2 {
  
  static int[] queue = new int[2_000_000];
  
  static int size = 0;
  static int front = 0;
  static int back = -1;
  
  static StringBuilder sb = new StringBuilder();
  
  public static void main(String[] args) throws Exception {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int N = Integer.parseInt(br.readLine());
    while(N-- > 0) {
      st = new StringTokenizer(br.readLine());
      String op = st.nextToken();
      if (op.equals("push")) push(Integer.parseInt(st.nextToken()));
      else if(op.equals("pop")) sb.append(pop() + "\n");
      else if(op.equals("size")) sb.append(size + "\n");
      else if(op.equals("empty")) sb.append(isEmpty()+"\n");
      else if(op.equals("front")) sb.append(front()+"\n");
      else if(op.equals("back")) sb.append(back()+"\n");
    }
    System.out.println(sb.toString());
  }
  static void push(int n) {
    queue[++back] = n;
    size++;
  }
  static int pop() {
    if(size >0) {
    front++;
    size--;
    return queue[front-1];
    }
    else return -1;
  }
  static int isEmpty() {
    if(size >0) return 0;
    else return 1;
  }
  static int front() {
    if(size>0) return queue[front];
    else return -1;
  }
  static int back() {
    if(size>0) return queue[back];
    else return -1;
  }
}

