package myListPackage;

public interface MyListIterator<E> {

	/**
	 * Inserts the specified element into the list.
	 * The element is inserted immediately before the element
	 * that would be returned by next(), if any.
	 * If the list contains no elements, the new element becomes
	 * the sole element on the list.
	 * @param x the element to insert
	 */
	void add(E x);
	
	/**
	 * Returns true if this list iterator has more elements
	 * when traversing the list in the forward direction.
	 * @return true if the list iterator has more elements
	 * when traversing the list in the forward direction
	 */
	boolean hasNext();

	/**
	 * Returns the next element in the list and advances
	 * the cursor position.
	 * @return the next element in the list
	 */
	E next();
	
	/**
	 * Removes from the list the last element that was returned
	 * by next().
	 */
	void remove();
	
	/**
	 * Replaces the last element returned by next() with the
	 * specified element.
	 * @param x the element with which to replace the last element
	 * returned by next
	 */
	void set(E x);
	
}
