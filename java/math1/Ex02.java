package math1;

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Ex02  {
  public static void main(String[] args) throws IOException {
  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  StringTokenizer st = new StringTokenizer(br.readLine());
  
  
  Long N = Long.parseLong(st.nextToken());
  int B = Integer.parseInt(st.nextToken());
  int namue = 0;
  ArrayList<Character> arr = new ArrayList<>();
  int i = 0;
  // N 나눌때마다 나머지가 하나씩 쌓인다.
  while(N > 0) {
    namue = (int)(N % B);
    N/=B;
    if(namue < 10) {
      arr.add((char)(namue + '0')) ;
    }
    else if(namue >=10) {
      arr.add((char)(namue - 10 + 'A'));
  }


  }
  for(int j = arr.size()-1; j >= 0; j-- ) {
    System.out.print(arr.get(j));
  }
}
}
