/**
 Determinar o piso da raiz de n
 */
/**
 * @author Isabela Gomes
 *
 */

package raiz;
import java.util.Scanner;

public class Raiz{

	public static void main (String[] args) {
		System.out.print ("Entre com um valor: ");
		try (Scanner valor = new Scanner (System.in)) {
			int n = valor.nextInt();
			int x = 0;
			for (int m = 1; (m*m) <= n; m++) {
				x = m;
			}
				System.out.print("O piso da raiz de " + n + " é " + x);
		}
	}
}


