import java.util.*;
import java.util.stream.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Integer n = Integer.parseInt(sc.nextLine());
            
            Integer[][] matrix = IntStream.range(0, n).mapToObj(i ->
                Stream.of(sc.nextLine().split(" ")).map(Integer::valueOf).toArray(Integer[]::new)
            ).toArray(Integer[][]::new);
            
            System.out.println(Math.abs(IntStream.range(0, n).map(i -> matrix[i][i] - matrix[i][n - i - 1]).sum()));
        }
    }
}
