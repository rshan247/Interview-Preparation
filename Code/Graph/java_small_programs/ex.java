import java.util.*;
class demo{

    static int gcd(int num1, int num2){
        while(num2 != 0){
            int temp = num2;
            num2 = num1%num2;
            num1 = temp;
        }
        return num1;
    }
    static int lcm(int num1, int num2){
        System.out.println(gcd(num1, num2));
        int lcm = (num1*num2) / gcd(num1, num2);
        return lcm;
    }

    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n1=sc.nextInt();
        int n2 = sc.nextInt();
        System.out.println(lcm(n1, n2));
    }
}