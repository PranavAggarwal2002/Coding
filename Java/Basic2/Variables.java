package Basic2;

public class Variables {
    public static void main(String[] args) {
        System.out.println("Type of Varibles");
        System.out.println("Interger(int, long, short, byte)");
        System.out.println("Float(float, double");
        System.out.println("Character(char)");
        System.out.println("Boolean(bool)");
    }
}

class Variables1_printlnVSprint {
    public static void main(String[] args) {
        System.out.print(45);
        System.out.print(45);
        System.out.println(45);
        System.out.println(45);
    }
}
//System.out.print(34)
//System.out.print(46)
//result will 3446
//System.out.println(34)
//System.out.println(46)
//reult will be
//34
//46
//println means print new line

class Variables2_integer {
    public static void main(String[] args) {
        int num = 3;
        System.out.println(num);
        int num1 = 3;
        int num2 = 5;
        int result = num1 + num2;
        System.out.println(result);
        byte by = 23;
        System.out.println(by);
        short sh = 23;
        System.out.println(sh);
        long l = 23344l; // for long we need to add l to number to let java know it is a long number
        System.out.println(l);
    }
}

class Variables3_float {
    public static void main(String[] args) {
        float num = 5.6f;
        double num1 = 1.2;
        System.out.println(num);
        System.out.println(num1);
    }
}
// float num = 5.6; is error as it assume deafault as double
// so for explecitly to use float we need to add 'f' to number

class Variables4_character {
    public static void main(String[] args) {
        char character = 'P';
        char character1 = '8';
        System.out.println(character);
        System.out.println(character1);
    }
}

class Variables5_boolean {
    public static void main(String[] args) {
        boolean b = true;
        System.out.println(b);
    }
}