package testList;
import static org.junit.Assert.*;

import org.junit.Test;

import myADT.MyArrayList;
import myADT.MyLinkedList;
import myADT.MyList;
import myADT.MyListIterator;

import java.util.NoSuchElementException;

public class TestMyList {

	public void testListOperations(MyList<Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		list.remove(1);
		list.remove(2);
		list.add(1, 6);
		list.add(2, 7);
		list.add(3, 8);
		list.set(4, 9);
		list.add(5, 10);
		list.add(0, 0);
		System.out.println(list);
		int x = list.get(0);
		assertEquals(x, 0);
		x = list.get(1);
		assertEquals(x, 1);
		x = list.get(2);
		assertEquals(x, 6);
		x = list.get(3);
		assertEquals(x, 7);
		x = list.get(4);
		assertEquals(x, 8);
		x = list.get(5);
		assertEquals(x, 9);
		x = list.get(6);
		assertEquals(x, 10);
		x = list.get(7);
		assertEquals(x, 5);
		try {
			x = list.get(8);
			assertTrue(false);
		} catch (IndexOutOfBoundsException e) {
			
		}
	}

	
	public void testListIterator(MyList<Integer> list) {
		list.add(1);
		list.add(2);
		list.add(3);
		list.add(4);
		list.add(5);
		MyListIterator<Integer> it = list.listIterator();
		it.add(0);
		int x = it.next();
		assertEquals(x, 1);
		it.add(6);
		it.add(7);
		it.add(8);
		x = it.next();
		assertEquals(x, 2);
		it.remove();
		x = it.next();
		assertEquals(x, 3);
		it.set(9);
		x = it.next();
		assertEquals(x, 4);
		it.remove();
		it.add(10);
		x = it.next();
		assertEquals(x, 5);
		assertFalse(it.hasNext());
		try {
			x = it.next();
			assertTrue(false);
		} catch (NoSuchElementException e) {
			//
		}
		System.out.println(list);
		MyListIterator<Integer> it2 = list.listIterator();
		x = it2.next();
		assertEquals(x, 0);
		x = it2.next();
		assertEquals(x, 1);
		x = it2.next();
		assertEquals(x, 6);
		x = it2.next();
		assertEquals(x, 7);
		x = it2.next();
		assertEquals(x, 8);
		x = it2.next();
		assertEquals(x, 9);
		x = it2.next();
		assertEquals(x, 10);
		x = it2.next();
		assertEquals(x, 5);
		try {
			x = it.next();
			assertTrue(false);
		} catch (NoSuchElementException e) {
			//
		}
	}

	@Test
	public void test1() {
		System.out.println("Start test1");
		testListOperations(new MyArrayList<Integer>());
		System.out.println("End test1");
	}

	@Test
	public void test2() {
		System.out.println("Start test2");
		testListIterator(new MyArrayList<Integer>());
		System.out.println("End test2");
	}

	@Test
	public void test3() {
		System.out.println("Start test3");
		testListOperations(new MyLinkedList<Integer>());
		System.out.println("End test3");
	}


	@Test
	public void test4() {
		System.out.println("Start test4");
		testListIterator(new MyLinkedList<Integer>());
		System.out.println("End test4");
	}

}
