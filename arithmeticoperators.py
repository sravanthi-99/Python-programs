#Arithmetic operators
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
public class MissingNumberFinder {
    public static void main(String[] args) {
        int[] arr = new int[99];
        int index = 0;

        // Fill array from 1 to 100, skip one number (e.g., 47)
        for (int i = 1; i <= 100; i++) {
            if (i != 47) {
                arr[index++] = i;
            }
        }

        // Calculate expected sum of 1 to 100
        int expectedSum = 100 * 101 / 2;

        // Calculate actual sum of array elements
        int actualSum = 0;
        for (int i = 0; i < arr.length; i++) {
            actualSum += arr[i];
        }

        // Find the missing number
        int missingNumber = expectedSum - actualSum;

        // Print result
        System.out.println("Missing number is: " + missingNumber);
    }
}
