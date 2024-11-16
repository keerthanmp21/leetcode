package InterviewImp;


import java.util.HashMap;
import java.util.Map;

public class CouponFinder2 {

    // Map for storing category names and their corresponding coupons
    private static Map<String, String> couponMap = new HashMap<>();
    
    // Map for storing category names and their parent categories
    private static Map<String, String> parentMap = new HashMap<>();

    // Method to initialize the coupon and category-parent mappings
    static {
        // Populate the couponMap
        couponMap.put("Comforter Sets", "Comforters Sale");
        couponMap.put("Bedding", "Savings on Bedding");
        couponMap.put("Bed & Bath", "Low price for Bed & Bath");

        // Populate the parentMap
        parentMap.put("Comforter Sets", "Bedding");
        parentMap.put("Bedding", "Bed & Bath");
        parentMap.put("Bed & Bath", "None");
        parentMap.put("Soap Dispensers", "Bathroom Accessories");
        parentMap.put("Bathroom Accessories", "Bed & Bath");
        parentMap.put("Toy Organizers", "Baby And Kids");
        parentMap.put("Baby And Kids", "None");
    }

    // Method to find the coupon for a given category
    public static String findCoupon(String category) {
        // Check if the category has a coupon
        if (couponMap.containsKey(category)) {
            return couponMap.get(category);
        }
        
        // If no coupon, check the parent category
        String parentCategory = parentMap.get(category);
        
        // If there is no parent category, return null
        if (parentCategory == null || parentCategory.equals("None")) {
            return null;
        }
        
        // Check the parent category
        return findCoupon(parentCategory);
    }

    public static void main(String[] args) {
        // Test the function with different categories
        System.out.println(findCoupon("Comforter Sets")); // Expected: Comforters Sale
        System.out.println(findCoupon("Bedding")); // Expected: Savings on Bedding
        System.out.println(findCoupon("Bathroom Accessories")); // Expected: Low price for Bed & Bath
        System.out.println(findCoupon("Soap Dispensers")); // Expected: Low price for Bed & Bath
        System.out.println(findCoupon("Toy Organizers")); // Expected: null
    }
}

