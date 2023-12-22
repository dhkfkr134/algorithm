import java.io.*;
import java.util.*;
public class Main{
public static void main(String[] args) throws IOException  {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    String B = st.nextToken();
    int N = Integer.parseInt(st.nextToken());
    int len = B.length();
    int sum = 0;
    for (int i = len-1 ; i >= 0 ; i--) {
      // 문자일때 처리
      if((int)B.charAt(i) >= 65) {
        sum += ((int)B.charAt(i) - 55) * Math.pow(N,len-1-i);
      }
      else {
        // Character.getNumbericValue(B.charAt(i))
        //  B.charAt(i) - '0'
        // Integer.parseInt((B.charAt(i)+" ").toString())
        sum += (B.charAt(i) - '0') *Math.pow(N,len-i-1);
      }
    }
    System.out.println(sum);
    

  }
}