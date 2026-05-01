package Basic5;

public class Conditionalstatements {
    public static void main(String[] args) {
        System.out.println("Conditional Statments");
    }
}

class ConditionalstatementsIfElse {
    public static void main(String[] args) {
        int x = 11;
        if(x>10)
            System.out.println("Hello");
        else
            System.out.println("Bye");
 
    }
}

/*class ConditionalstatementsIfTrueFalse {
    public static void main(String[] args) {
        int x = 11;
        if(true)
            System.out.println("Hello"); //this will get printed

        int y = 11;
        if(false)
            System.out.println("Bye"); //this will not get printed
 
    }
}*/

class ConditionalstatementsIfElse2 {
    public static void main(String[] args) {
        int x = 13;
        int y = 12;
        if(x>y)
        {
            System.out.println("Hello");
            System.out.println("Thank You");
        }
        else
            System.out.println("Bye");
 
    }
}

class ConditionalstatementsIfElseif {
    public static void main(String[] args) {
        int x = 13;
        int y = 12;
        int z = 11;
        if(x>y && x>z)
            System.out.println(x);
        else if(y>x && y>z)
            System.out.println(y);
        else
            System.out.println(z);
 
    }
}

class ConditionalstatementsIfElseifefficient {
    public static void main(String[] args) {
        int x = 13;
        int y = 12;
        int z = 11;
        if(x>y && x>z)
            System.out.println(x);
        else if(y>z)
            System.out.println(y);
        else
            System.out.println(z);
 
    }
}