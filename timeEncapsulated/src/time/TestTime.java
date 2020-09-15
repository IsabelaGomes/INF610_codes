package time;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestTime {

	void testConstructor(Time t) {
		assertEquals(12, t.getHour());
		assertEquals(30, t.getMinute());
		assertEquals(5, t.getSecond());
	}
	
	void t() {
		Time t1 = null, t2 = null;
		System.out.println(t1.toString());
		System.out.println(t1.getMinute());
		System.out.println(t1.difference(t2));
		t1.setHour(11);
		System.out.println(t1.toString());
	}
	
	void testGetSet(Time t) {
		t.setHour(12);
		t.setMinute(30);
		t.setSecond(5);
		int h = t.getHour();
		assertEquals(12, h);
		int m = t.getMinute();
		assertEquals(30, m);
		int s = t.getSecond();
		assertEquals(5, s);
		boolean b = t.setHour(25);
		assertFalse(b);
		assertEquals(12, t.getHour());
		assertEquals(30, t.getMinute());
		assertEquals(5, t.getSecond());
		b = t.setMinute(40);
		assertTrue(b);
		assertEquals(12, t.getHour());
		assertEquals(40, t.getMinute());
		assertEquals(5, t.getSecond());
		b = t.setSecond(20);
		assertTrue(b);
		assertEquals(12, t.getHour());
		assertEquals(40, t.getMinute());
		assertEquals(20, t.getSecond());
	}
	
	void testCompare(Time t1, Time t2) {
		assertEquals(t1.compareTo(t2), -1);
		assertEquals(t2.compareTo(t1), 1);
		assertEquals(t1.compareTo(t1), 0);
	}
	
	void testDifference(Time t1, Time t2) {
		t1.setHour(12);
		t1.setMinute(30);
		t1.setSecond(20);
		t2.setHour(12);
		t2.setMinute(30);
		t2.setSecond(40);
		int d = t1.difference(t2);
		assertEquals(d, -20);
		t2.setHour(0);
		t2.setMinute(32);
		t2.setSecond(22);
		d = t1.difference(t2);
		assertEquals(d, 43078);
	}

	@Test
	public void test1() {
		Time t1 = new Time1(12, 30, 5);
		System.out.println(t1);
		testConstructor(t1);
		Time t2 = new Time2(12, 30, 5);
		System.out.println(t2);
		testConstructor(t2);
	}
	
	@Test
	public void test2() {
		Time t1 = new Time1();
		testGetSet(t1);
		Time t2 = new Time2();
		testGetSet(t2);
	}
	
	@Test
	public void test3() {
		Time t1a = new Time1(12, 30, 20), t1b = new Time1(12, 30, 25);
		testCompare(t1a, t1b);
		Time t2a = new Time2(12, 30, 20), t2b = new Time2(12, 30, 25);
		testCompare(t2a, t2b);
	}
	
	@Test
	public void test4() {
		Time t1a = new Time1(), t1b = new Time1();
		testDifference(t1a, t1b);
		Time t2a = new Time2(), t2b = new Time2();
		testDifference(t2a, t2b);
	}

}
