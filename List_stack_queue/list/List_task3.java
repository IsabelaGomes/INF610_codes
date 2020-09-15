/*(3) Using iterators, write a function that receives a list of Integer elements and returns true if the list is non decreasing (there is no element 
 * that is smaller than a previous one). The function must return false, otherwise.*/

package list;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class List_task3 {
	
	public boolean isNonDecreasing(List<Integer> lista) {
		int k = lista.size();
		if(lista.isEmpty()) {
			return true;
		}
		else if (k == 1) {
			return true;
		}
		else {
			Iterator<Integer> it1 = lista.iterator();
			Iterator<Integer> it2 = lista.iterator();
			int x1, x2;
			x1 = it1.next();
			while(it1.hasNext() && it2.hasNext()){
				x1 = it1.next();
				x2 = it2.next();
				if(x2 > x1) {
					return false;
				}		
			}
			return true;
		}
	}

	public static void main(String[] args) {
		
		List_task3 listaobg = new List_task3();
		
		List<Integer> lista = new ArrayList<Integer>();
		lista.add(8);  
		lista.add(12);  
		lista.add(19); 
		lista.add(21); 
		lista.add(29);
		
		boolean dec = listaobg.isNonDecreasing(lista);
				
		if (dec == true) {
			System.out.print("A lista não é decrescente.");
		}
		else {
			System.out.print("A lista é decrescente.");
		}
	}
}
