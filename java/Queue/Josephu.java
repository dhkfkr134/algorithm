package Queue;

import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Josephu {
  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    LinkedList<Integer> q = new LinkedList<>();
    int pos = 0;
    String result ="<";
    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());
    
    for(int i = 0; i < N; i++ ) {
      q.add(i+1);
    }
    for(int i=0;i < N-1; i++) {
      pos = (pos+K-1) % (q.size());
      result = result + q.remove(pos)+", ";
    }
    result = result + q.getFirst()+">";
    System.out.println(result);
  }
}
