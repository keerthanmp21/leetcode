package InterviewImp;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

public class CouponFinder {

    private static String findCoupon(String catogoryName, List<Map<String, String>> coupons, 
    List<Map<String, String>> categories){
        Map<String, String> couponMap = new HashMap<>();
        for(Map<String, String> coupon: coupons){
            couponMap.put(coupon.get("CategoryName"), coupon.get("CouponName"));
        }

        Map<String, String> parentMap = new HashMap<>();
        for(Map<String, String> categorie: categories){
            parentMap.put(categorie.get("CategoryName"), categorie.get("CategoryParentName"));
        }

        return getCouponForCategory(catogoryName, couponMap, parentMap);
    }

    private static String getCouponForCategory(String category, Map<String, String> couponMap,
    Map<String, String> parentMap){
        if(couponMap.containsKey(category)){
            return couponMap.get(category);
        }

        String parentCategory = parentMap.get(category);

        if("None".equals(parentCategory)){
            return null;
        }

        return getCouponForCategory(parentCategory, couponMap, parentMap);
    }

    public static void main(String[] args) {
        List<Map<String, String>> coupons = new ArrayList<>();
        Map<String, String> coupon1 = new HashMap<>();
        coupon1.put("CategoryName", "Comforter Sets");
        coupon1.put("CouponName", "Comforters Sale");
        Map<String, String> coupon2 = new HashMap<>();
        coupon2.put("CategoryName", "Bedding");
        coupon2.put("CouponName", "Savings on Bedding");
        Map<String, String> coupon3 = new HashMap<>();
        coupon3.put("CategoryName", "Bed & Bath");
        coupon3.put("CouponName", "Low price for Bed & Bath");
        
        coupons.add(coupon1);
        coupons.add(coupon2);
        coupons.add(coupon3);

        List<Map<String, String>> categories = new ArrayList<>();
        Map<String, String> category1 = new HashMap<>();
        category1.put("CategoryName", "Comforter Sets");
        category1.put("CategoryParentName", "Bedding");
        Map<String, String> category2 = new HashMap<>();
        category2.put("CategoryName", "Bedding");
        category2.put("CategoryParentName", "Bed & Bath");
        Map<String, String> category3 = new HashMap<>();
        category3.put("CategoryName", "Bed & Bath");
        category3.put("CategoryParentName", "None");
        Map<String, String> category4 = new HashMap<>();
        category4.put("CategoryName", "Soap Dispensers");
        category4.put("CategoryParentName", "Bathroom Accessories");
        Map<String, String> category5 = new HashMap<>();
        category5.put("CategoryName", "Bathroom Accessories");
        category5.put("CategoryParentName", "Bed & Bath");
        Map<String, String> category6 = new HashMap<>();
        category6.put("CategoryName", "Toy Organizers");
        category6.put("CategoryParentName", "Baby And Kids");
        Map<String, String> category7 = new HashMap<>();
        category7.put("CategoryName", "Baby And Kids");
        category7.put("CategoryParentName", "None");
        
        categories.add(category1);
        categories.add(category2);
        categories.add(category3);
        categories.add(category4);
        categories.add(category5);
        categories.add(category6);
        categories.add(category7);
        
        System.out.println(findCoupon("Comforter Sets", coupons, categories)); // Output: Comforters Sale
        System.out.println(findCoupon("Bedding", coupons, categories)); // Output: Savings on Bedding
        System.out.println(findCoupon("Bathroom Accessories", coupons, categories)); // Output: Low price for Bed & Bath
        System.out.println(findCoupon("Soap Dispensers", coupons, categories)); // Output: Low price for Bed & Bath
        System.out.println(findCoupon("Toy Organizers", coupons, categories));  // Output: null
    }
}
