package dictionary.impl;

import dictionary.interfaces.Dictionary;

public class HashTable<K extends Comparable<K>,V> implements Dictionary<K,V> {

	private Object table[];
	private int size;
		
	public HashTable(int size) {
		this.size = size;
		table = new Object[size];
	}
	
	public void put(K key, V value) {
		int h = key.hashCode() % size;
		if (table[h] == null) {
			table[h] = new LinkedListDictionary<K,V>();
		}
		((Dictionary<K,V>) table[h]).put(key, value);
	}

	public V get(K key) {
		int h = key.hashCode() % size;
		if (table[h] == null) {
			return null;
		}
		return ((Dictionary<K,V>) table[h]).get(key);
	}
		
	public String toString() {
		String s = "{\n";
		for(int i = 0; i < size; ++i) {
			ListDictionary<K,V> list = (ListDictionary<K,V>) table[i];
			if (list != null) {
				s += list.toString2();
			}
		}
		s += "}";
		return s;
	}


}
