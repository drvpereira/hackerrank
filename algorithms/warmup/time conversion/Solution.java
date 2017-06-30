import java.util.*;

public class Solution {

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            String s = in.nextLine();
            
            char half = s.charAt(8);
            int hour = Integer.parseInt(s.substring(0, 2)), 
                minute = Integer.parseInt(s.substring(3, 5)), 
                second = Integer.parseInt(s.substring(6, 8));
            
            if (hour == 12 && half == 'A' || hour != 12 && half == 'P') {
                hour = (hour + 12) % 24;
            }
            
            System.out.printf("%02d:%02d:%02d\n", hour, minute, second);
        }
    }
}
