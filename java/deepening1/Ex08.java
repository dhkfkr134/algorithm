/*
 * https://www.acmicpc.net/problem/25206
 * 
 */
package deepening1;
import java.util.Scanner;
import java.util.StringTokenizer;
public class Ex08 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    float result = 0;
    float gradesum = 0;
    for(int i =0; i < 20; i++) {
      StringTokenizer st = new StringTokenizer(scanner.nextLine());
      st.nextToken();
      Float num = Float.parseFloat(st.nextToken());
      String grade = st.nextToken();
      if (!grade.equals("P")) {
        System.out.printf("%d : !P\n",i);
        gradesum += num;
      }
      if (grade.equals("A+")) {
        result += (num * 4.5f);
      }
      else if(grade.equals("A0")) {
        result += (num * 4.0f);
      }
      else if(grade.equals("B+")) {
        result += (num * 3.5f);
      }
      else if(grade.equals("B0")) {
        result += (num * 3.0f);
      }
      else if(grade.equals("C+")) {
        result += (num * 2.5f);
      }
      else if(grade.equals("C0")) {
        result += (num * 2.0f);
      }
      else if(grade.equals("D+")) {
        result += (num * 1.5f);
      }
      else if(grade.equals("D0")) {
        result += (num * 1.0f);
      }
      else ;
      System.out.printf("result/gradesum : %f, result : %f, greadesum : %f\n", result/gradesum ,result, gradesum);
    }
    
    System.out.println(result/gradesum);
  }
}
