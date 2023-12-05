// faster 10811
package array;
import java.io.*;
import java.util.StringTokenizer;

public class Baekjoon10811_1 {
  public static void main(String[] args) throws IOException {
    
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    
    int[] basket = new int[N];
    
    for(int i = 0; i<N; i++) {
      basket[i] = i+1;
    }
    
    for(int j =0; j< M; j++) {
      
      st = new StringTokenizer(br.readLine());
      
      int x = Integer.parseInt(st.nextToken());
      
      int y = Integer.parseInt(st.nextToken());
      
      for(int l = x-1 ; l <(x+y)/2;l++) {
       
          int temp = basket[l];
          basket[l] = basket[x+y-l-2];
          basket[x+y-l-2] = temp;
        
      }
    }
    
    for(int k = 0; k < N; k++) {
      bw.write(basket[k] + " ");
    }
    
    br.close();
    bw.flush();
    bw.close();
    
  }
}
