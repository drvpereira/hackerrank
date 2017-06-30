import java.util.Scanner;
import java.util.stream.Stream;

public class Solution {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
			sc.nextLine();
        	int result = Stream.of(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).sum();
        	System.out.println(result);
        }
    }
}
