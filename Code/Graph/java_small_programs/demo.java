
import java.util.Scanner;

class demo
{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
       String s=sc.nextLine();
       for(int i=0;i<s.length();i+=2){
       char c=s.charAt(i);
       int f=Character.getNumericValue(s.charAt(i+1));
       for(int j=0;j<f;j++){
        System.out.print(c);
       }}
    }

}