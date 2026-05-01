package Basic5;

public class Ternaryoperator {
    public static void main(String[] args) {
        System.out.println("Termary Operator");
}
}

class NonTernaryoperatorIfElse {
    public static void main(String[] args) {
        int x = 11;
        int result = 0;
        if(x%2==0)
            result = 10;
        else
            result = 20;
        System.out.println(result);
    }
}

class TernaryoperatorIfElse {
    public static void main(String[] args) {
        int x = 11;
        int result = 0;
        result = x%2==0 ? 10 : 20;
        System.out.println(result);
    }
}

class TernaryoperatorIfElseif {
    public static void main(String[] args) {
        int x = 11;
        int result = 0;

        result = (x % 2 == 0) ? 10 : (x % 3 == 0) ? 20 : 30;

        System.out.println(result);
    }
}
// result = cond1 ? val1 : cond2 ? val2 : cond3 ? val3 : val4;