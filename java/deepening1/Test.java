package deepening1;

public class Test {
  public static void main(String[] args) {
    String str = "asdfasdfasdf";
    if(str.contains("a")) {
      System.out.println(str.replace("af", "!"));
    }
  }
}
