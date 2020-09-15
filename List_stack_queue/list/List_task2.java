/*(2) Using iterators, write a generic Java function that receives a List of elements of type E and a value of type E. 
 * The function must return the number of occurrences of the given value inside the list.*/

package list;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class List_task2 {
		
	public <E> int occurences (List<E> lista, E element) {
		if(lista.isEmpty()) {
			return -1;
		}
		else {
			int occ = 0;
			Iterator<E> it = lista.iterator();
			while(it.hasNext()) {
				E valor = it.next();
				if(valor.equals(element)) {
					occ++;
				}			
			}		
			return occ;
		}
	}

	public static void main(String[] args) {
		
		List_task2 lista_int = new List_task2();
		List<Integer> lista_i = new ArrayList<Integer>();
		lista_i.add(1);  // 1
		lista_i.add(8);  // 1, 8
		lista_i.add(29); // 1, 8, 29
		lista_i.add(1); // 1, 8, 29, 14
		lista_i.add(157); // 1, 8, 29, 14, 157
		
		List_task2 lista_str = new List_task2();
		List<Character> lista_s = new ArrayList<Character>();
		lista_s.add('I');  
		lista_s.add('s');  
		lista_s.add('a'); 
		lista_s.add('b'); 
		lista_s.add('e'); 
		lista_s.add('l');
		lista_s.add('a');
		
		int e_i = 7;		
		char e_s = 'a';
		
		int occ_i = lista_int.occurences(lista_i, e_i);
		int occ_s = lista_str.occurences(lista_s, e_s);
		
		if (occ_i == -1) {
			System.out.println("Não há ocorrências.");
		}
		else {
			System.out.println("Há " + occ_i + " ocorrência(s) de " + e_i);
		}
		if (occ_s == -1) {
			System.out.println("Não há ocorrências.");
		}
		else {
			System.out.println("Há " + occ_s + " ocorrência(s) de " + e_s);
		}
	}
}