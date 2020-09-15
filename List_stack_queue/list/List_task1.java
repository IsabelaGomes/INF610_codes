//(1) Using iterators, write a Java function that receives a non-empty list of Integer elements and return the largest one.

package list;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class List_task1 {
	
	public int findMax(List<Integer> lista) {
		if(lista.isEmpty()) {
			return -1;
		}
		else {
			Iterator<Integer> it1 = lista.iterator();
			int x, max;
			max = 0;
			
			while(it1.hasNext()) {
				x = it1.next();
				if(x > max) {
					max = x;
				}			
			}		
			return max;
		}
	}

	public static void main(String[] args) {
		
		List_task1 listaobg = new List_task1();
		
		List<Integer> lista = new ArrayList<Integer>();
		lista.add(1);  // 1
		lista.add(8);  // 1, 8
		lista.add(29); // 1, 8, 29
		lista.add(14); // 1, 8, 29, 14
		lista.add(157); // 1, 8, 29, 14, 157
		//List<Integer> lista1 = new ArrayList<Integer>();
				
		int maximo = listaobg.findMax(lista);
		
		if (maximo == -1) {
			System.out.print("A lista está vazia");
		}
		else {
			System.out.print("O valor máximo da lista é " + maximo);
		}
	}
}