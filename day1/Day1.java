import java.io.*;
import java.util.*;

public class Day1 {
    public static void main(String[] args) {
        List<Integer> ls1 = new ArrayList<>();
        List<Integer> ls2 = new ArrayList<>();
        String filename = "test.txt";

        try (Scanner sc = new Scanner(new File(filename))) {
            while (sc.hasNext()) {
                String line = sc.nextLine();
                String[] parts = line.split("\\s+"); // split by whitespace
                int num1 = Integer.parseInt(parts[0]);
                int num2 = Integer.parseInt(parts[1]);

                ls1.add(num1);
                ls2.add(num2);
            }
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println(e.getMessage());
        }

        Collections.sort(ls1);
        Collections.sort(ls2);

        // part 1
        int distance = 0; 
        for (int i = 0; i < ls1.size(); i++) {
            distance += Math.abs(ls1.get(i) - ls2.get(i));
        }
        System.out.printf("distance is %d%n", distance);

        // part 2
        Set<Integer> hashset = new HashSet<>(ls1);
        Map<Integer, Integer> hashmap = new HashMap<>();
        int similarity = 0; 
        
        for (Integer num : ls2) {
            if (hashset.contains(num)) {
                hashmap.put(num, hashmap.getOrDefault(num, 0)+1);
            }
        }

        for (Integer num : ls1) {
            similarity += hashmap.getOrDefault(num, 0) * num;
        }

        System.out.printf("similarity score is %d%n", similarity);
    }    
}
