import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.next();
        String b = sc.next();

        int alength = a.length();
        int blength = b.length();

        if (alength==blength){
            System.out.printf("same");
        } else if (alength>blength) {
            System.out.printf("%s %d",a,alength);
        } else {
            System.out.printf("%s %d",b,blength);
        }
    }
}