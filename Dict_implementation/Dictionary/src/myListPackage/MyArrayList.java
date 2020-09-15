package myListPackage;
import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;
import java.util.NoSuchElementException;


public class MyArrayList<E> extends AbstractList<E> implements MyList<E> {

	private static int DEFAULT_SIZE = 100;
	private int size;
	private E elements[];
	
	public MyArrayList(int max) {
		this.size = 0;
		this.elements = (E[]) new Object[max];
	}
	
	public MyArrayList() {
		this(DEFAULT_SIZE);
	}

	public void add(E x) {
		if (size == elements.length) {
			throw new IllegalStateException("List full");
		}
		elements[size] = x;
		++size;
	}

	public void add(int i, E x) {
		if (i < 0 || i > size) {
			throw new IndexOutOfBoundsException();
		}
		for(int j = size; j > i; --j) {
			elements[j] = elements[j-1];
		}
		elements[i] = x;
		++size;
	}

	public void clear() {
		size = 0;
	}

	public E get(int i) {
		if (i < 0 || i >= size) {
			throw new IndexOutOfBoundsException();
		}
		return elements[i];
	}

	public boolean isEmpty() {
		return size != 0;
	}

	public MyListIterator<E> listIterator() {
		return new ArrayListIterator();
	}

	public void remove(int i) {
		if (i < 0 || i >= size) {
			throw new IndexOutOfBoundsException();
		}
		for(int j = i; j < size-1; ++j) {
			elements[j] = elements[j+1];
		}
		--size;
	}

	public void set(int i, E x) {
		if (i < 0 || i >= size) {
			throw new IndexOutOfBoundsException();
		}
		elements[i] = x;
	}

	public int size() {
		return size;
	}

	
	// -------------------- Internal class: ArrayListIterator
	
	
	private class ArrayListIterator implements MyListIterator<E> {
		
		private int pos;
		
		public ArrayListIterator() {
			pos = 0;
		}
		
		public void add(E x) {
			if (size == elements.length) {
				throw new IllegalStateException("List full");
			}
			for(int i = size; i > pos; --i) {
				elements[i] = elements[i-1];
			}
			elements[pos] = x;
			++size;
			++pos;
		}

		public boolean hasNext() {
			return pos < size;
		}
		
		public E next() {
			if (pos >= size) {
				throw new NoSuchElementException("Invalid position");
			}
			E e = elements[pos];
			++pos;
			return e;
		}

		public void remove() {
			if (pos == 0 || pos > size) {
				throw new IllegalStateException("Invalid position");
			}
			for(int i = pos; i < size; ++i) {
				elements[i-1] = elements[i];
			}
			--size;
			--pos;
		}

		public void set(E x) {
			if (pos == 0 || pos > size) {
				throw new IllegalStateException("Invalid position");
			}
			elements[pos-1] = x;
		}
		
	}
	
	
}
