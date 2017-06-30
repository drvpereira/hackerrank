import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

	private static PriorityQueue<Integer> min = new PriorityQueue<>(10, new Comparator<Integer>() {
        public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    });
    private static PriorityQueue<Integer> max = new PriorityQueue<>();

    public static void add(Integer n) {
    	if (min.size() <= max.size()) {    		
    		min.add(n);
    	} else {
    		max.add(n);
    	}

    	balance();
    }

    public static void balance() {
    	if (!min.isEmpty() && !max.isEmpty() && min.peek() > max.peek()) {
	    	Integer minHead = min.poll();
	    	Integer maxHead = max.poll();

	    	min.add(maxHead);
	    	max.add(minHead);
    	}
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        
        for(int a_i=0; a_i < n; a_i++){
            add(in.nextInt());
            if (min.size() == max.size())
            	System.out.printf("%.1f\n", (min.peek() + max.peek())/2.0);
            else
            	System.out.printf("%.1f\n", min.peek() * 1.0);
        }

    }
}
