/* https://www.acmicpc.net/problem/11718
 * 
 */
package string;

import java.io.*;

public class Baekjoon11718_1 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
  
    String str = "";
  
    while((str = br.readLine()) != null) {
      bw.write(str);
      System.out.println(str);
    }
   
    br.close();
    bw.flush();
    bw.close();
  
}
}
