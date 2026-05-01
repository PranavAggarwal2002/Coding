package Basic6;

public class BAdvanceSwitchstatements {
    public static void main(String[] args) {
        System.out.println(" Advance Switch Statments");
    }
}

class OldSwitchstatements {
    public static void main(String[] args) {
        String day = "Monday";
        switch(day){
            case "Saturday", "Sunday":
                System.out.println("6am");
                break;
            case "Monday":
                System.out.println("8am");
                break;
            default:
                System.out.println("7am");
        }
    }
}

class AdvanceSwitchstatements {
    public static void main(String[] args) {
        String day = "Monday";
        switch(day){
            case "Saturday", "Sunday" -> System.out.println("6am");
            case "Monday" -> System.out.println("8am");
            default -> System.out.println("7am");
        }
    }
}

class AdvanceSwitchstatements2 {
    public static void main(String[] args) {
        String day = "Monday";
        String result = "";
        switch(day){
            case "Saturday", "Sunday" -> result = "6am";
            case "Monday" -> result = "8am";
            default -> result = "7am";
        }
        System.out.println(result);
    }
}


class AdvanceSwitchstatementsasExpression {
    public static void main(String[] args) {
        String day = "Monday";
        String result = "";
        result = switch(day){
            case "Saturday", "Sunday" -> "6am";
            case "Monday" -> "8am";
            default -> "7am";
        };
        System.out.println(result);
    }
}

class AdvanceSwitchstatementsasExpressionwithoutarrowkey {
    public static void main(String[] args) {
        String day = "Monday";
        String result = "";
        result = switch(day){
            case "Saturday", "Sunday" : yield "6am";
            case "Monday" : yield "8am";
            default : yield "7am";
        };
        System.out.println(result);
    }
}