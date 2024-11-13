package InterviewImp;

public class LargeNumberAddition {
    public static String parseAndValidate(String str) throws IllegalArgumentException{
        String cleaned = str.replace(",", "");

        if(!cleaned.matches("[0-9]+")){
            throw new IllegalArgumentException("Input contain invalid characters");
        }

        return cleaned;
    }

    public static String addNumbersWithCommas(String num1, String num2) throws IllegalArgumentException{
        String cleanedString1 = parseAndValidate(num1);
        String cleanedString2 = parseAndValidate(num2);

        String result = addStrings(cleanedString1, cleanedString2);

        return formatWithString(result);
    }

    public static String addStrings(String num1, String num2){
        StringBuilder result = new StringBuilder();
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int carry = 0;

        while(i >= 0 || j >= 0 || carry != 0){
            int digit1 = (i >= 0) ? num1.charAt(i) - '0' : 0;
            int digit2 = (j >= 0) ? num2.charAt(j) - '0' : 0;

            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            result.append(sum % 10);

            i--;
            j--;
        }

        return result.reverse().toString();
    }

    private static String formatWithString(String number){
        StringBuilder formatted = new StringBuilder(number);
        int N = formatted.length();

        for(int i = N - 3; i > 0; i -= 3){
            formatted.insert(i, ',');
        }

        return formatted.toString();
    }

    private static String fibonacci(int n){
        if(n <= 0){
            throw new IllegalArgumentException("Fibonacci number should be positive");
        }

        String a = "0";
        String b = "1";

        for(int i = 2; i <= n; i++){
            String temp = addNumbersWithCommas(a, b);
            a = b;
            b = temp;
        }

        return b;
    }

    public static void main(String[] args) {
        try{
            String num1 = "1,234,567,890";
            String num2 = "987,654,321";
            String sum = addNumbersWithCommas(num1, num2);
            System.out.println("Sum with commas: " + sum);

            int n = 25;
            String fibResult = fibonacci(n);
            System.out.println("Fibonacci(" + n + "): " + fibResult) ;
        }
        catch(IllegalArgumentException e){
            System.out.println("Error: " + e.getMessage());
        }
    }
}
