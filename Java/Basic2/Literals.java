package Basic2;

public class Literals {
    public static void main(String[] args) {
        // Literals
        int num1 = 0b101;
        System.out.println(num1);
        int num2 = 0x101;
        System.out.println(num2);
        int num3 = 0x7E;
        System.out.println(num3);
        int num4 = 10_00_00_000;// print as 100000000, but underscore help us to know number of zeroes
        System.out.println(num4);
        double num5 = 56;
        System.out.println(num5);
        double num6 = 12e7;// is equal to 12 into 10 raise to power 7
        System.out.println(num6);
        char c = 'a';
        c++;//c will have increment c = c + 1, answer will b
        System.out.println(c);
    }
}
