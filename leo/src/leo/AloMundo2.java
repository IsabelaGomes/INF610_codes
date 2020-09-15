package leo;

import java.util.Scanner;

public class AloMundo2 {

    public static void main(String[] args) {
        String nome = ""; 
        Scanner dig_us = new Scanner(System.in);
        
        System.out.print("Qual seu nome? ");
        nome = dig_us.nextLine();
        System.out.println("Oi, "+ nome);
    }   
}