package myADT;

public interface MyList<E> {
	
	/**
	 * Appends the specified element to the end of this list.
	 * @param x element to be appended to this list
	 */
	void add(E x);

	/**
	 * Inserts an element at the specified position in this list.
	 * @param i index at which the specified element is to be inserted
	 * @param x element to be inserted
	 */
	void add(int i, E x);

	/**
	 * Removes all of the elements from this list.
	 */
	void clear();
	
	/**
	 * Returns the element at the specified position in this list.
	 * @param i index of the element to return
	 * @return the element at the specified position in this list
	 */
	E get(int i);
	
	/**
	 * Returns true if this list contains no elements.
	 * @return true if this list contains no elements
	 */
	boolean isEmpty();
	
	/**
	 * Returns a list iterator over the elements in this list.
	 * @return a list iterator over the elements in this list
	 */
	MyListIterator<E> listIterator();

	/**
	 * Removes the element at the specified position in this list.
	 * @param i the index of the element to be removed
	 */
	void remove(int i);
	
	/**
	 * Replaces the element at the specified position in this list
	 * ith the specified element.
	 * @param i index of the element to replace
	 * @param x  element to be stored at the specified position
	 */
	void set(int i, E x);
	
	/**
	 * Returns the number of elements in this list.
	 * @return the number of elements in this list
	 */
	int size();

}
