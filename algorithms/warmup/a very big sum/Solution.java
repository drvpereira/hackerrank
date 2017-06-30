import java.util.Scanner;
import java.util.stream.Stream;

public class Solution {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
			sc.nextLine();
        	Long result = Stream.of(sc.nextLine().split(" ")).mapToLong(Long::valueOf).sum();
        	System.out.println(result);
        }
    }
}