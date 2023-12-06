// 머리를 탁치는 풀이!
package string;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon5622 {
  public static void main(String[] args) throws IOException {
   
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    String str = br.readLine();
    int result = str.length();
    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);
      result += (ch - 'A' + 6) / 3;
      // 이런방법 익숙해지자. if ch in "XVYZ": result-=1
      if("XVYZ".indexOf(ch) != -1) {
        result -= 1;
      }
    }
    System.out.println(result);
  }
     
}
 
