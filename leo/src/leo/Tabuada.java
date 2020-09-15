package leo;

import java.util.Scanner;

public class Tabuada {           
    
    public static void main(String[] args) {
        int n = 0;
        String valorLido = "";  
        
        Scanner dig_us = new Scanner(System.in);
        
        System.out.print("Informe um numero: ");
        valorLido = dig_us.nextLine();
        n = Integer.parseInt(valorLido);
        for(int i = 1; i <= 10; i++) {
	        System.out.println(n + " x " + i + " = " + (n*i));
        }
    }
}