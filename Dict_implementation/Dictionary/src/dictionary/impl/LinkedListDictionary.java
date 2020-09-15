package dictionary.impl;

import myListPackage.MyLinkedList;

public class LinkedListDictionary<K extends Comparable<K>,V> extends ListDictionary<K,V> {
	
	public LinkedListDictionary() {
		super(new MyLinkedList<ListDictionary.ListNode<K,V>>());
	}
	
}
