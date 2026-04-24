package Basic3;

public class Conversioncasting {
    public static void main(String[] args) {
        byte b = 127;
        int a = 257;
        // b = a will give error as short term cannot be bigger term since int is bigger than byte
        // b = a even if a = 12 will not work
        // a = b will work adn this called conversion
        b = (byte)a; // this is called casting changing type to put value
        System.out.println(b);
    }
}

class Conversioncasting2floatint {
    public static void main(String args[]) {
        float f = 5.6f;
        // int x = f; will give error
        int x = (int) f; // due to int x = 5 as it will drop .6
        System.out.println(x);
    }
} 

class Conversioncasting3typepromotion {
    public static void main(String args[]) {
        byte g = 10;
        byte h = 30;
        int result = g * h;
        // type promotion as result will be bigger than byte so error
        System.out.println(result);
    }
} 