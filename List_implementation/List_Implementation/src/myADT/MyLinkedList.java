package myADT;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.NoSuchElementException;


class Node<E> {
	E value;
	Node<E> next, previous;
}

public class MyLinkedList<E> extends AbstractList<E> implements MyList<E> {
	
	private Node<E> tail;
	
	public MyLinkedList() {
		tail = new Node<E>();
		tail.next = tail;
		tail.previous = tail;
	}
			
	public void add(E x) {
		Node<E> n = new Node<E>();
		n.value = x;
		n.next = tail;
		n.previous = tail.previous;
		tail.previous.next = n;
		tail.previous = n;
	}
	
	private Node<E> moveToPosition(int i) {
		Node<E> n = tail.next;
		while (i > 0) {
			if (n == tail) {
				throw new IndexOutOfBoundsException();
			}
			n = n.next;
			--i;
		}
		return n;
	}
	
	public E get(int i) {
		Node<E> n = moveToPosition(i);
		if (n == tail) {
			throw new IndexOutOfBoundsException();
		}
		return n.value;
	}

	public void add(int i, E x) {
		Node<E> n = moveToPosition(i);
		Node<E> n1 = new Node<E>();
		n1.value = x;
		n1.next = n;
		n1.previous = n.previous;
		n.previous.next = n1;
		n.previous = n1;
	}

	public void remove(int i) {
		Node<E> n = moveToPosition(i);
		if (n == tail) {
			throw new IndexOutOfBoundsException();
		}
		n.previous.next = n.next;
		n.next.previous = n.previous;
	}

	public void set(int i, E x) {
		Node<E> n = moveToPosition(i);
		if (n.next == null) {
			throw new IndexOutOfBoundsException();
		}
		n.value = x;
	}

	public int size() {
		Node<E> n = tail.next;
		int i = 0;
		while (n != tail) {
			n = n.next;
			++i;
		}
		return i;
	}

	public boolean isEmpty() {
		return tail.next == tail;
	}

	public void clear() {
		tail.next = tail;
		tail.previous = tail;
	}
	
	public MyListIterator<E> listIterator() {
		return new LinkedListIterator();
	}
	
	
	// -------------------- Internal class: ArrayListIterator
	
	
	class LinkedListIterator implements MyListIterator<E> {
		
		private Node<E> pos;
		
		public LinkedListIterator() {
			pos = tail.next;
		}
		
		public boolean hasNext() {
			return pos != tail;
		}

		public E next() {
			if (pos == tail) {
				throw new NoSuchElementException("Invalid position");
			}
			E e = pos.value;
			pos = pos.next;
			return e;
		}

		public void add(E x) {
			Node<E> n1 = new Node<E>();
			n1.value = x;
			n1.next = pos;
			n1.previous = pos.previous;
			pos.previous.next = n1;
			pos.previous = n1;
		}

		public void set(E x) {
			if (pos.previous == tail) {
				throw new NoSuchElementException("Invalid position");
			}
			pos.previous.value = x;
		}

		public void remove() {
			if (pos.previous == tail) {
				throw new IllegalStateException("Invalid position");				
			}
			pos.previous.previous.next = pos;
			pos.previous = pos.previous.previous;
		}
	
	}
	

}
