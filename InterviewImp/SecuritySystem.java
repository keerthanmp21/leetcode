package InterviewImp;

import java.util.*;

public class SecuritySystem {

    public static List<List<String>> processRecords(List<List<String>> records) {
        Set<String> inside = new HashSet<>(); // Employees currently inside the room
        Set<String> exitedWithoutEnter = new HashSet<>(); // Employees who exited without entering
        Set<String> enteredWithoutExit = new HashSet<>(); // Employees who entered without exiting
        
        // Process each record
        for (List<String> record : records) {
            String employee = record.get(0);
            String action = record.get(1);
            
            if (action.equals("enter")) {
                if (!inside.contains(employee)) {
                    inside.add(employee); // Add to the inside set
                }
            } else if (action.equals("exit")) {
                if (inside.contains(employee)) {
                    inside.remove(employee); // Remove from inside set as they exit
                } else {
                    exitedWithoutEnter.add(employee); // They exit without entering
                }
            }
        }
        
        // Employees who entered but didn't exit
        enteredWithoutExit.addAll(inside);
        
        // Convert sets to sorted lists
        List<String> enteredWithoutExitList = new ArrayList<>(enteredWithoutExit);
        List<String> exitedWithoutEnterList = new ArrayList<>(exitedWithoutEnter);
        
        Collections.sort(enteredWithoutExitList);
        Collections.sort(exitedWithoutEnterList);
        
        return Arrays.asList(enteredWithoutExitList, exitedWithoutEnterList);
    }

    public static void main(String[] args) {
        // Test cases
        List<List<String>> records1 = Arrays.asList(
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Pauline", "exit"),
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Paul", "exit"),
            Arrays.asList("Martha", "exit"),
            Arrays.asList("Joe", "enter"),
            Arrays.asList("Martha", "enter"),
            Arrays.asList("Steve", "enter"),
            Arrays.asList("Martha", "exit"),
            Arrays.asList("Jennifer", "enter"),
            Arrays.asList("Joe", "enter"),
            Arrays.asList("Curtis", "exit"),
            Arrays.asList("Curtis", "enter"),
            Arrays.asList("Joe", "exit"),
            Arrays.asList("Martha", "enter"),
            Arrays.asList("Martha", "exit"),
            Arrays.asList("Jennifer", "exit"),
            Arrays.asList("Joe", "enter"),
            Arrays.asList("Joe", "enter"),
            Arrays.asList("Martha", "exit"),
            Arrays.asList("Joe", "exit"),
            Arrays.asList("Joe", "exit")
        );

        System.out.println(processRecords(records1)); // Expected: [["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]]

        List<List<String>> records2 = Arrays.asList(
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Paul", "exit")
        );
        System.out.println(processRecords(records2)); // Expected: [[], []]

        List<List<String>> records3 = Arrays.asList(
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Paul", "exit"),
            Arrays.asList("Paul", "exit")
        );
        System.out.println(processRecords(records3)); // Expected: [["Paul"], ["Paul"]]

        List<List<String>> records4 = Arrays.asList(
            Arrays.asList("Raj", "enter"),
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Paul", "exit"),
            Arrays.asList("Paul", "exit"),
            Arrays.asList("Paul", "enter"),
            Arrays.asList("Raj", "enter")
        );
        System.out.println(processRecords(records4)); // Expected: [["Raj", "Paul"], ["Paul"]]
    }
}
