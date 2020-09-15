package leo;

import java.util.Scanner;

public class Trocadevalores {

    public static void main(String[] args) {

        String nome1;
        String nome2;
        String aux;
        Scanner dig_us = new Scanner(System.in);
        nome1 = " mestre do universo";
        nome2 = "";
        System.out.println("Troca valores entre variaveis");
        System.out.print("Qual o seu nome?: ");
        nome2 = dig_us.nextLine();
        aux = nome2;
        nome2 = nome1;
        nome1 = aux;   
        System.out.println(nome1 + nome2);
    } 
}