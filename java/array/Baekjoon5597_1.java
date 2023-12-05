// faster 5597
package array;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon5597_1 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    boolean[] students = new boolean[30];
    
    for(int i = 0 ; i < 28; i++) {
      students[Integer.parseInt(br.readLine())-1] = true;
    }
    
    for(int j = 0; j < 30; j++) {
      if(students[j] == false) System.out.println(j+1);
    }
    
    br.close();
  }
}
