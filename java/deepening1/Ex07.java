package deepening1;

import java.util.Scanner;
public class Ex07 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String[] string = {"c=","c-","dz=","d-","lj","nj","s=","z="};
    
    String st = scanner.nextLine();
    
    for(int i = 0; i <string.length; i++) {
      if(st.contains(string[i]))
          st = st.replace(string[i], "a");
    }
    System.out.print(st.length());
  }
  
}
