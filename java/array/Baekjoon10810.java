/*
 * https://www.acmicpc.net/problem/10813
 *
 *
 * System.out, System.in 대신 io Stream중 문자열을 다루는 InputStreamReader OutputStreamWriter를 사용하여 Stream을
 * 다루고 BufferedReader와 BufferedWriter를 사용해서 버퍼를 통해 문자열을 입출력했다. => 빠른 입출력 속도를 위해서
 *
 */
package array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Baekjoon10810 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken(" "));
    int M = Integer.parseInt(st.nextToken());
    int[] arr = new int[N];

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());

      int I = Integer.parseInt(st.nextToken());
      int J = Integer.parseInt(st.nextToken());
      int K = Integer.parseInt(st.nextToken());

      for (int j = I - 1; j < J; j++) {
        arr[j] = K;
      }
    }
    for (int k = 0; k < arr.length; k++) {
      bw.write(arr[k] + " ");
    }
    br.close();
    bw.flush();
    bw.close();
  }
}
