/*
 * https://www.acmicpc.net/problem/5597
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
import java.util.Arrays;
import java.util.StringTokenizer;

public class Baekjoon5597 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;
    int[] attendance = new int[28];
    for (int i = 0; i < 28; i++) {
      st = new StringTokenizer(br.readLine());
      attendance[i] = Integer.parseInt(st.nextToken());
    }
    for (int j = 1; j < 31; j++) {
      int count = 0;
      for (int k : attendance) {
        if (j == k) {
          break;
        } else {
          count++;
        }
      }
      if (count == 28)
        bw.write(j + "\n");
    }
    br.close();
    bw.flush();
    bw.close();

  }
}
