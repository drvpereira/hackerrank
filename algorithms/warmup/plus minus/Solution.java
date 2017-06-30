import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            in.nextLine();
            Double[] arr = Stream.of(in.nextLine().split(" ")).map(Double::valueOf).toArray(Double[]::new);
            
            Double positives = 1.0 * Stream.of(arr).filter(i -> i > 0).count();
            Double negatives = 1.0 * Stream.of(arr).filter(i -> i < 0).count();
            Double zeroes = 1.0 * Stream.of(arr).filter(i -> i == 0).count();
            Double total = positives + negatives + zeroes;
            
            System.out.printf("%.6f\n", positives / total);
            System.out.printf("%.6f\n", negatives / total);
            System.out.printf("%.6f\n", zeroes / total);
        }
    }
}
