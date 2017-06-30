import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class Solution {

    static List<Long> solve(List<Integer> a, List<Integer> b) {
        Supplier<IntStream> diff = () -> IntStream.range(0, a.size()).map(i -> a.get(i) - b.get(i));
        Long alice = diff.get().filter(i -> i > 0).count();
        Long bob = diff.get().filter(i -> i < 0).count();
        return Arrays.asList(alice, bob);
    }

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            List<Integer> a = Stream.of(in.nextLine().split(" ")).map(Integer::valueOf).collect(Collectors.toList());
            List<Integer> b = Stream.of(in.nextLine().split(" ")).map(Integer::valueOf).collect(Collectors.toList());
            
            List<Long> result = solve(a, b);
            
            result.stream().forEach(i -> System.out.print(i + " "));
        }
    }
}
