package tests;
import static org.junit.Assert.*;

import org.junit.Test;

import dictionary.impl.AVLTree;
import dictionary.impl.BTree;
import dictionary.impl.BinarySearchTree;
import dictionary.impl.LinkedListDictionary;
import dictionary.impl.HashTable;
import dictionary.impl.ArrayListDictionary;
import dictionary.interfaces.Dictionary;

public class TestOperations {

	void testOperations(Dictionary<Integer, String> d) {
		d.put(1, "One");
		d.put(9, "nine");
		d.put(5, "five");
		d.put(3, "three");
		d.put(1, "one");
		d.put(4, "four");
		d.put(6, "six");
		d.put(8, "eight");
		d.put(7, "seven");
		System.out.println(d);
		assertTrue(d.get(1).equals("one"));
		assertTrue(d.get(3).equals("three"));
		assertTrue(d.get(4).equals("four"));
		assertTrue(d.get(5).equals("five"));
		assertTrue(d.get(6).equals("six"));
		assertTrue(d.get(7).equals("seven"));
		assertTrue(d.get(8).equals("eight"));
		assertTrue(d.get(9).equals("nine"));
		assertEquals(d.get(2), null);
	}
	
	@Test
	public void test1() {
		System.out.println("\nTest ArrayList implementation");
		Dictionary<Integer, String> d = new ArrayListDictionary<Integer,String>(100);
		testOperations(d);
	}

	@Test
	public void test2() {
		System.out.println("\nTest LinkedList implementation");
		Dictionary<Integer, String> d = new LinkedListDictionary<Integer,String>();
		testOperations(d);
	}

	@Test
	public void test3() {
		System.out.println("\nTest BinarySearchTree implementation");
		Dictionary<Integer, String> d = new BinarySearchTree<Integer,String>();
		testOperations(d);
	}

	@Test
	public void test4() {
		System.out.println("\nTest AVLTree implementation");
		Dictionary<Integer, String> d = new AVLTree<Integer, String>();
		testOperations(d);
	}

	@Test
	public void test5() {
		System.out.println("\nTest BTree implementation");
		Dictionary<Integer, String> d = new BTree<Integer, String>(2);
		testOperations(d);
	}

	@Test
	public void test6() {
		System.out.println("\nTest HashTable implementation");
		Dictionary<Integer, String> d = new HashTable<Integer, String>(1000);
		testOperations(d);
	}

	
}
