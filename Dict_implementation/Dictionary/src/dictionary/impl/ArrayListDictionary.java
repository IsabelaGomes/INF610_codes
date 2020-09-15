package dictionary.impl;

import myListPackage.MyArrayList;

/**
 * Implementation of Dictionary using List with an array and binary search.
 */
public class ArrayListDictionary<K extends Comparable<K>,V> extends ListDictionary<K,V> {
	
	public ArrayListDictionary(int size) {
		super(new MyArrayList<ListDictionary.ListNode<K,V>>());
	}
	
	public void put(K key, V value) {
		int i = 0;
		while (i < list.size()) {
			ListNode<K,V> x = list.get(i);
			if (key.equals(x.key)) {
				x.value = value;
				return;
			} else if (key.compareTo(x.key) < 0) {
				break;
			}
			++i;
		}
		ListNode<K,V> y = new ListNode<K,V>();
		y.key = key;
		y.value = value;
		list.add(i, y);
	}
	
	public V get(K key) {
		int size = list.size();
		int i = 0, j = size-1;
		while (i <= j) {
			int k = (i + j) / 2;
			ListNode<K,V> x = list.get(k);
			int r = key.compareTo(x.key);
			if (r < 0) {        // key < x.key
				j =  k - 1;
			} else if (r > 0) { // kay > x.key
				i = k + 1;
			} else {            // key == x.key
				return x.value;
			}
		}
		return null;
	}

	

}
