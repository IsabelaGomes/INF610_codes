package testList;
import static org.junit.Assert.*;

import org.junit.Test;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.List;
import java.util.NoSuchElementException;

public class TesJSDKtList {

	void testListOperations(List<Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.remove(1);
		list.remove(2);
		list.add(1, 6);
		list.add(2, 7);
		list.add(3,8);
		list.set(4,9);
		list.add(5,10);
		System.out.println(list);
		int x = list.get(0);
		assertEquals(1, x);
		x = list.get(1);
		assertEquals(6, x);
		x = list.get(2);
		assertEquals(7, x);
		x = list.get(3);
		assertEquals(8, x);
		x = list.get(4);
		assertEquals(9, x);
		x = list.get(5);
		assertEquals(10, x);
		x = list.get(6);
		assertEquals(5, x);
		try {
			x = list.get(7);
			assertTrue(false);
		} catch (IndexOutOfBoundsException e) {
			
		}
	}

	
	void testListIterator(List<Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		ListIterator<Integer> it = list.listIterator();
		int x = it.next();
		assertEquals(1, x);
		it.add(6);
		it.add(7);
		it.add(8);
		x = it.next();
		assertEquals(2, x);
		it.remove();
		x = it.next();
		assertEquals(3, x);
		it.set(9);
		x = it.next();
		assertEquals(4, x);
		it.remove();
		try {
			it.remove();
			assertTrue(false);
		} catch (IllegalStateException e) {
			//
		}
		it.add(10);
		x = it.next();
		assertEquals(5, x);
		assertFalse(it.hasNext());
		try {
			x = it.next();
			assertTrue(false);
		} catch (NoSuchElementException e) {
			//
		}
		System.out.println(list);
		ListIterator<Integer> it2 = list.listIterator();
		x = it2.next();
		assertEquals(1, x);
		x = it2.next();
		assertEquals(6, x);
		x = it2.next();
		assertEquals(7, x);
		x = it2.next();
		assertEquals(8, x);
		x = it2.next();
		assertEquals(9, x);
		x = it2.next();
		assertEquals(10, x);
		x = it2.next();
		assertEquals(5, x);
		try {
			x = it.next();
			assertTrue(false);
		} catch (NoSuchElementException e) {
			//
		}
	}

	
	void testPrevious(List<Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.add(6);
		ListIterator<Integer> it = list.listIterator();
		assertFalse(it.hasPrevious());
		int x = it.next();
		assertEquals(1, x);
		assertTrue(it.hasPrevious());
		x = it.previous();
		assertEquals(1, x);
		x = it.next();
		assertEquals(1, x);
		x = it.next();
		assertEquals(2, x);
		it.remove();
		x = it.previous();
		assertEquals(1, x);
		x = it.next();
		assertEquals(1, x);
		x = it.next();
		assertEquals(3, x);
		x = it.next();
		assertEquals(4, x);
		x = it.next();
		assertEquals(5, x);
		x = it.next();
		assertEquals(6, x);
		x = it.previous();
		assertEquals(6, x);
		x = it.previous();
		assertEquals(5, x);
		it.remove();
		x = it.previous();
		assertEquals(4, x);
		it.remove();
		x = it.next();
		assertEquals(6, x);
		it.remove();
		x = it.previous();
		assertEquals(3, x);
		ListIterator<Integer> it2 = list.listIterator();
		x = it2.next();
		assertEquals(1, x);		
		x = it2.next();
		assertEquals(3, x);
		assertFalse(it2.hasNext());
		System.out.println(list);
	}

	
	@Test
	public void test1() {
		System.out.println("Start test1");
		testListOperations(new ArrayList<Integer>());
		System.out.println("End test1");
	}

	@Test
	public void test2() {
		System.out.println("Start test2");
		testListIterator(new ArrayList<Integer>());
		System.out.println("End test2");
	}

	@Test
	public void test3() {
		System.out.println("Start test3");
		testListOperations(new LinkedList<Integer>());
		System.out.println("End test3");
	}

	@Test
	public void test4() {
		System.out.println("Start test4");
		testListIterator(new LinkedList<Integer>());
		System.out.println("End test4");
	}

	@Test
	public void test5() {
		System.out.println("\nTesting MyIterator.previous()...");
		testPrevious(new ArrayList<Integer>());
		testPrevious(new LinkedList<Integer>());
	}

}
