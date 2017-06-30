import java.util.*;

public class Solution {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int n = in.nextInt(), noSteps = 1;
            
            while(noSteps <= n) {
                for (int i = 0; i < n - noSteps; i++) System.out.print(" ");
                for (int i = 0; i < noSteps; i++) System.out.print("#");
                System.out.println();
                noSteps++;
            }
        }
    }
}