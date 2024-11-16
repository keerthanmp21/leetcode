package InterviewImp;
import java.text.DecimalFormat;
import java.util.*;
import java.text.SimpleDateFormat;

public class CouponFinder3 {
    
}


class DiscountCalculator {

    // Data Structures
    static class Coupon {
        String couponName;
        String dateModified;
        String discount;

        public Coupon(String couponName, String dateModified, String discount) {
            this.couponName = couponName;
            this.dateModified = dateModified;
            this.discount = discount;
        }

        public String getDiscount() {
            return discount;
        }
    }

    static class Product {
        String productName;
        double price;
        String categoryName;

        public Product(String productName, double price, String categoryName) {
            this.productName = productName;
            this.price = price;
            this.categoryName = categoryName;
        }

        public double getPrice() {
            return price;
        }

        public String getCategoryName() {
            return categoryName;
        }
    }

    // Maps to store coupon and parent data
    private static Map<String, List<Coupon>> couponMap = new HashMap<>();
    private static Map<String, String> parentMap = new HashMap<>();
    private static Map<String, Product> productMap = new HashMap<>();

    // Initialize coupon, parent and product data
    static {
        // Coupons
        couponMap.put("Comforter Sets", Arrays.asList(
                new Coupon("Comforters Sale", "2020-01-01", "10%"),
                new Coupon("Cozy Comforter Coupon", "2020-01-01", "$15")
        ));
        
        couponMap.put("Bedding", Arrays.asList(
                new Coupon("Best Bedding Bargains", "2019-01-01", "35%"),
                new Coupon("Savings on Bedding", "2019-01-01", "25%")
        ));
        
        couponMap.put("Bed & Bath", Arrays.asList(
                new Coupon("Low price for Bed & Bath", "2018-01-01", "50%"),
                new Coupon("Bed & Bath extravaganza", "2019-01-01", "75%")
        ));

        // Parent categories
        parentMap.put("Comforter Sets", "Bedding");
        parentMap.put("Bedding", "Bed & Bath");
        parentMap.put("Bed & Bath", null); // Root category with no parent
        parentMap.put("Soap Dispensers", "Bathroom Accessories");
        parentMap.put("Bathroom Accessories", "Bed & Bath");
        parentMap.put("Toy Organizers", "Baby And Kids");
        parentMap.put("Baby And Kids", null); // Root category with no parent

        // Products
        productMap.put("Cozy Comforter Sets", new Product("Cozy Comforter Sets", 100.00, "Comforter Sets"));
        productMap.put("All-in-one Bedding Set", new Product("All-in-one Bedding Set", 50.00, "Bedding"));
        productMap.put("Infinite Soap Dispenser", new Product("Infinite Soap Dispenser", 500.00, "Bathroom Accessories"));
        productMap.put("Rainbow Toy Box", new Product("Rainbow Toy Box", 257.00, "Baby And Kids"));
    }

    // Method to find the coupon for a given category
    public static Coupon findCoupon(String category) {
        // Check the coupon for the current category
        List<Coupon> coupons = couponMap.get(category);
        
        if (coupons == null || coupons.isEmpty()) {
            // If no coupons for this category, check its parent category
            String parentCategory = parentMap.get(category);
            if (parentCategory == null) {
                return null; // No coupon found in the hierarchy
            }
            return findCoupon(parentCategory); // Recursively check parent
        }

        // If multiple coupons exist, find the most recent one
        Coupon validCoupon = null;
        Date latestDate = new Date(0); // Initialize to a very old date

        for (Coupon coupon : coupons) {
            // Convert the DateModified string to a Date object
            Date couponDate = parseDate(coupon.dateModified);
            if (couponDate.after(latestDate)) {
                latestDate = couponDate;
                validCoupon = coupon;
            }
        }

        return validCoupon;
    }

    // Helper method to parse date string
    private static Date parseDate(String dateStr) {
        try {
            return new SimpleDateFormat("yyyy-MM-dd").parse(dateStr);
        } catch (Exception e) {
            return null;
        }
    }

    // Method to apply coupon and calculate discounted price for a product
    public static String applyCoupon(String productName) {
        // Find the product
        Product product = productMap.get(productName);
        if (product == null) {
            return null; // Product not found
        }

        // Find the applicable coupon for the product's category
        Coupon coupon = findCoupon(product.getCategoryName());

        if (coupon == null) {
            return String.format("%.2f", product.getPrice()); // No coupon available, return original price
        }

        // Parse and apply the discount
        String discount = coupon.getDiscount();
        double price = product.getPrice();

        if (discount.endsWith("%")) {
            // Percentage discount
            double percentage = Double.parseDouble(discount.replace("%", ""));
            price -= price * (percentage / 100);
        } else if (discount.startsWith("$")) {
            // Flat discount
            double flatAmount = Double.parseDouble(discount.replace("$", ""));
            price -= flatAmount;
        }

        // Return discounted price formatted to 2 decimal places
        DecimalFormat df = new DecimalFormat("#.00");
        return df.format(price);
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(applyCoupon("Cozy Comforter Sets")); // Expected: 85.00
        System.out.println(applyCoupon("All-in-one Bedding Set")); // Expected: 37.50
        System.out.println(applyCoupon("Infinite Soap Dispenser")); // Expected: 250.00
        System.out.println(applyCoupon("Rainbow Toy Box")); // Expected: 257.00 (no discount)
    }
}

