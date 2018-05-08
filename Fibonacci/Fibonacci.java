/**
 * Recursive Fibonacci series in Java using IntelliJ IDEA IDE
 */
import java.util.Scanner;
public class Fibonacci {

     int Recursive(int n){

        if(n<0) {
            System.out.println("Wrong Value for N");
        }
        else if(n==1){
            return 0;
        }
        else if(n==2){
            return 1;
        }
        else{
            return Recursive(n-1)+Recursive(n-2);
        }
        return 0;
    }

    public static void main(String[] args) {

        Fibonacci myFib = new Fibonacci(); //declared Fibonacci class
        Scanner sc = new Scanner(System.in); //setup on screen input system

        System.out.print("Enter number of Fibonacci iterations: ");
        int n = sc.nextInt(); //read Int value input from console
        System.out.println();

        for (int i = 1; i < n+1; i++){
            System.out.print(myFib.Recursive(i) + " ");
        }
        System.out.println();
    }
}
