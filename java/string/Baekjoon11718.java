/* https://www.acmicpc.net/problem/11718
 * 
 */
package string;

import java.io.*;

public class Baekjoon11718 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//  
//    while(true) {
//      String str = br.readLine();
//      bw.write(str+"\n");
//      if(str == null || str.isEmpty()) break;
//      System.out.print(bw);
//    }
//   
//    br.close();
//    bw.flush();
//    bw.close();

StringBuilder builder = new StringBuilder();
while(true){
    String str = br.readLine();
    if (str == null || str.isEmpty()) {
        break;
    }
    builder.append(str).append("\n");
}
br.close();
System.out.println(builder);
}
}
