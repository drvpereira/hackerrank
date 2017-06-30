import java.util.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int n = in.nextInt(), count = 0, max = 0;
            
            for (int i = 0; i < n; i++){
                int element = in.nextInt();
                if (element > max) {
                    count = 1;
                    max = element;
                } else if (element == max) {
                    count++;
                }
            }
            
            System.out.println(count);
        }
    }
}
