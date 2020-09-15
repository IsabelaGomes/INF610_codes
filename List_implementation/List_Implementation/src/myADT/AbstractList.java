package myADT;

public abstract class AbstractList<E> implements MyList<E> {

	public String toString() {
		String s = "[";
		MyListIterator<E> it = listIterator();
		if (it.hasNext()) {
			s += it.next().toString();
		}
		while(it.hasNext()) {
			s += "," + it.next().toString();
		}
		s += "]";
		return s;
	}

}
