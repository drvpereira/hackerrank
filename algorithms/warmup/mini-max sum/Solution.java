import java.util.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            long total = 0;
            int min = Integer.MAX_VALUE, max = 0;
            
            while (in.hasNextInt()) {
                int element = in.nextInt();
                total += element;
                if (element > max) max = element;
                if (element < min) min = element;
            }
            
            System.out.println((total - max) + " " + (total - min));
        }
    }
}
