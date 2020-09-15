/**
 * 
 */
/**
 * @author Isabela Gomes
 *
 */
package gcd;

public class Gcd{

	public static void main (String[] args) {
		
		int a = 31415;
		int b = 14142; 
		int ct = 1;
		while (b > 0) {
			int rest = a%b;
			a = b;
			b = rest;
			ct++; 
			}
		System.out.print("The gcd is " + a + " and it took " + ct + " steps to solve it.");
	}
}