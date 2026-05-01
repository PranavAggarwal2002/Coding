package Basic6;

public class ASwitchstatements {
    public static void main(String[] args) {
        System.out.println("Switch Statments");
    }
}

class Nonswitchstatements {
    public static void main(String[] args) {
        int n = 1;
        if(n==1)
        System.out.println("Monday");
        else if(n==2)
        System.out.println("Tuesday");
        else if(n==3)
        System.out.println("Wednesday");
        else if(n==4)
        System.out.println("Thursday");
        else if(n==5)
        System.out.println("Friday");
        else if(n==6)
        System.out.println("Saturday ");
        else
        System.out.println("Sunday");
    }
}

class SwitchstatementsEx {
    public static void main(String[] args) {
        System.out.println("Switch Statments");
        int n = 1;
        switch(n){
            case 1:
            System.out.println("Monday");
            case 2:
            System.out.println("Tuesday");
            case 3:
            System.out.println("Wednesday");
            case 4:
            System.out.println("Thursday");
            case 5:
            System.out.println("Friday");
            case 6:
            System.out.println("Saturday");
            case 7:
            System.out.println("Sunday");
        }
    }
}
class SwitchstatementsExwithbreak {
    public static void main(String[] args) {
        System.out.println("Switch Statments");
        int n = 1;
        switch(n){
            case 1:
            System.out.println("Monday");
            break;
            case 2:
            System.out.println("Tuesday");
            break;
            case 3:
            System.out.println("Wednesday");
            break;
            case 4:
            System.out.println("Thursday");
            break;
            case 5:
            System.out.println("Friday");
            break;
            case 6:
            System.out.println("Saturday");
            break;
            case 7:
            System.out.println("Sunday");
            break;
        }
    }
}

class SwitchstatementsExwithbreakanddefault {
    public static void main(String[] args) {
        System.out.println("Switch Statments");
        int n = 9;
        switch(n){
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Enter a Valid Number");
        }
    }
}