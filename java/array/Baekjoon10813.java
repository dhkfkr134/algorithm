/*
 * https://www.acmicpc.net/problem/10813
 *
 *
 *
 *
 */
package array;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Baekjoon10813 {

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());
    int[] arr = new int[N];
    for (int i = 0; i < N; i++) {
      arr[i] = i + 1;
    }
    for (int j = 0; j < M; j++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      int temp = arr[x - 1];
      arr[x - 1] = arr[y - 1];
      arr[y - 1] = temp;
    }
    for (int k = 0; k < N; k++) {
      bw.write(arr[k] + " ");
    }
    br.close();
    bw.flush();
    bw.close();



  }
}
