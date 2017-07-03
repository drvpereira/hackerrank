import java.util.*;
import java.util.stream.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            String line = scan.nextLine().trim();
            if (line.isEmpty()) {
                System.out.println(0);
            } else {
                String[] tokens = line.split("[ !,?._'@]+");
                System.out.println(tokens.length);
                Stream.of(tokens).forEach(System.out::println);
            }
        }
    }
}
