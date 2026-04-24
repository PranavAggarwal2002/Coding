package Basic4;

public class R1Arithmeticoperators {
    public static void main(String args[]) {
        System.out.println("Arithmetic Opearators Functions");
    }
}

class ArithmeticoperatorsAddition {
    public static void main(String args[]) {
        int num1 = 7;
        System.out.println("num1 is " + num1);
        int num2 = 5;
        System.out.println("num2 is " + num2);
        int result = num1 + num2;
        System.out.println("Addition of num1 and num2");
        System.out.println(result);
    }
}

class ArithmeticoperatorsSubtraction {
    public static void main(String args[]) {
        int num1 = 7;
        System.out.println("num1 is " + num1);
        int num2 = 5;
        System.out.println("num2 is " + num2);
        int result = num1 - num2;
        System.out.println("Subtraction of num1 and num2");
        System.out.println(result);
    }
}

class ArithmeticoperatorsMultiplication {
    public static void main(String args[]) {
        int num1 = 7;
        System.out.println("num1 is " + num1);
        int num2 = 5;
        System.out.println("num2 is " + num2);
        int result = num1 * num2;
        System.out.println("Multiplication of num1 and num2");
        System.out.println(result);
    }
}

class ArithmeticoperatorsDivision {
    public static void main(String args[]) {
        int num1 = 7;
        System.out.println("num1 is " + num1);
        int num2 = 5;
        System.out.println("num2 is " + num2);
        int result = num1 / num2;
        System.out.println("Quotient(/) of num1 and num2");
        System.out.println(result);
        int result1 = num1 % num2;
        System.out.println("Remainder(%) of num1 and num2");
        System.out.println(result1);
    }
}

class ArithmeticoperatorsIncrementandDecrement {
    public static void main(String args[]) {
        int num = 7;
        System.out.println("num is " + num);
        num = num + 2;
        System.out.println("Num increment by 2, num = num + 2");
        System.out.println(num);
        num += 2;
        System.out.println("Num increment/add by 2 shortcut, num += 2");
        System.out.println(num);
        num -= 2;
        System.out.println("Num decrement/sub by 2 shortcut, num -= 2");
        System.out.println(num);
        num *= 2;
        System.out.println("Num mutiply by 2 shortcut, num *= 2");
        System.out.println(num);
        num++;
        System.out.println("Num increment by 1 shortcut, num++, post - increment");
        System.out.println(num);
        ++num;
        System.out.println("Num increment by 1 shortcut, ++num, pre - increment");
        System.out.println(num);
        num--;
        System.out.println("Num decrement by 1 shortcut, num--");
        System.out.println(num);
    }
}
// int num = 7;
// int result = ++num; increment the value first and then fetch the value
// Sustem.out.println(result); is 8

// int num = 7;
// int result = num++; fetch the value first and then increment the value
// Sustem.out.println(result); is 7