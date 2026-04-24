package Basic4;

public class R3Logicaloperators {
    public static void main(String args[]) {
        System.out.println("Logical Opearators Functions");
    }
}

class Logicaloperatorsand {
    public static void main(String args[]) {
        int x = 5;
        System.out.println("num 1 is " + x);
        int y = 7;
        System.out.println("num 2 is " + y);
        int w = 6;
        System.out.println("num 3 is " + w);
        int v = 4;
        System.out.println("num 4 is " + v);
        boolean result = x > y & w > v;
        System.out.println("result = x > y & w > v");
        System.out.println(result);
    }
}

class Logicaloperatorsandshortcircuit {
    public static void main(String args[]) {
        int x = 5;
        System.out.println("num 1 is " + x);
        int y = 7;
        System.out.println("num 2 is " + y);
        int w = 6;
        System.out.println("num 3 is " + w);
        int v = 4;
        System.out.println("num 4 is " + v);
        boolean result = x > y && w > v;
        System.out.println("result = x > y && w > v");
        System.out.println("What short circuit do in and is is that if first condition is false, it will not excecute second condition at all");
        System.out.println(result);
    }
}

class Logicaloperatorsor {
    public static void main(String args[]) {
        int x = 5;
        System.out.println("num 1 is " + x);
        int y = 7;
        System.out.println("num 2 is " + y);
        int w = 6;
        System.out.println("num 3 is " + w);
        int v = 4;
        System.out.println("num 4 is " + v);
        boolean result = x > y | w > v;
        System.out.println("result = x > y | w > v");
        System.out.println(result);
    }
}

class Logicaloperatorsorshortcircuit {
    public static void main(String args[]) {
        int x = 5;
        System.out.println("num 1 is " + x);
        int y = 7;
        System.out.println("num 2 is " + y);
        int w = 6;
        System.out.println("num 3 is " + w);
        int v = 4;
        System.out.println("num 4 is " + v);
        boolean result = x > y || w > v || x > 1;
        System.out.println("result = x > y || w > v || x > 1");
        System.out.println("What short circuit do in or is is that if first condition is true, it will not excecute second condition at all");
        System.out.println(result);
    }
}

class Logicaloperatorsnot {
    public static void main(String args[]) {
        int x = 5;
        System.out.println("num 1 is " + x);
        int y = 7;
        System.out.println("num 2 is " + y);
        boolean result = x > y;
        System.out.println("result = x > y, while println(!result)");
        System.out.println(!result);
    }
}