package dictionary.impl;

import dictionary.interfaces.Dictionary;
import myListPackage.MyList;
import myListPackage.MyListIterator;


public class ListDictionary<K extends Comparable<K>,V> implements Dictionary<K,V> {
	
	protected MyList<ListNode<K,V>> list;
	
	protected static class ListNode<K,V> {
		protected K key;
		protected V value;				
	}
		
	public ListDictionary(MyList<ListNode<K,V>> list) {
		this.list = list;
	}
	
	public void put(K key, V value) {
		MyListIterator<ListNode<K,V>> it = list.listIterator();
		while (it.hasNext()) {
			ListNode<K,V> x = it.next();
			if (key.equals(x.key)) { // found the key
				x.value = value;     // updates associated value
				return;              // returns immediately
			}
		}
		// key was not found
		ListNode<K,V> y = new ListNode<K,V>(); // create new node
		y.key = key;
		y.value = value;
		list.add(y);     // insert new node at the end of the list
	}

	public V get(K key) {
		MyListIterator<ListNode<K,V>> it = list.listIterator();
		while (it.hasNext()) {
			ListNode<K,V> x = it.next();
			if (key.equals(x.key)) { // found the key
				return x.value;      // returns associated value
			}
		}
		return null;
	}
	
	public String toString() {
		String s = "{\n" + toString2() + "}";
		return s;
	}
	
	public String toString2() {
		String s = "";
		MyListIterator<ListNode<K,V>> it = list.listIterator();
		while (it.hasNext()) {
			ListNode<K,V> x = it.next();
			s += x.key + "->" + x.value + "\n";
		}
		return s;
	}

}
