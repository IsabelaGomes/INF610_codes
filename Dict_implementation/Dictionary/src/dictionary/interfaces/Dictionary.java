package dictionary.interfaces;

/**
 * An association of keys to values.
 * 
 * @param <K> The type of the keys.
 * @param <V> The type of the values associated with the keys
 */
public interface Dictionary<K extends Comparable<K>,V> {
	
	/**
	 * Inserts or updates an association (key => value)
	 * @param key a unique identifier
	 * @param value the value associated with the identifier
	 */
	void put(K key, V value);
	
	/**
	 * Obtains the value associated with the given key
	 * @param key a unique identifier
	 * @return the value associated with the given key;
	 * if there is no such value, returns null
	 */
	V get(K key);

}

