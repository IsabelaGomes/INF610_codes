package leo;

import java.util.Scanner;

public class Mediaaluno {
	
    public static void main(String[] args) {  
    	
        String nome = "";
        float n1 = 0; 
        float n2 = 0;
        float n3 = 0;
        float n4 = 0;
        double total = 0; 
        double media = 0;
        Scanner dig_us = new Scanner(System.in);
       
        System.out.print("Qual e o seu nome:");
        nome = dig_us.nextLine();
        
        System.out.print("Informe a 1 nota:");
        n1 = dig_us.nextFloat();
        
        System.out.print("Informe a 2 nota:");
        n2 = dig_us.nextFloat();
        
        System.out.print("Informe a 3 nota:");
        n3 = dig_us.nextFloat();
        
        System.out.print("Informe a 4 nota:");
        n4 = dig_us.nextFloat();
        
        total = n1+n2+n3+n4;
        media = total/4;
        
        System.out.println(nome+", a sua media e " + media);
    }
}