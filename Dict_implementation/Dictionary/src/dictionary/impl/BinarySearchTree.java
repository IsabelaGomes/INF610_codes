package dictionary.impl;

import dictionary.interfaces.Dictionary;

public class BinarySearchTree <K extends Comparable<K>, V>
implements Dictionary<K, V> {

	private Node root;
	
	class Node {
		private K key;
		private V value;
		private BinarySearchTree<K, V> left, right;
		public Node(K key, V value) {
			this.key = key;
			this.value = value;
			this.left = createNewTree();
			this.right = createNewTree();
		}
	}
	
	public BinarySearchTree() {
		root = null;
	}

	public void put(K key, V value) {
		if (isEmpty()) {
			setRoot(createNewNode(key, value));
		} else if (key.compareTo(getKey()) == 0){
			root.value = value;
		} else if (key.compareTo(getKey()) < 0) {
			getLeft().put(key, value);
		} else {
			getRight().put(key, value);
		}
	}

	public V get(K key) {
		if (isEmpty()) {
			return null;
		} else if (key.compareTo(getKey()) == 0){
			return root.value;
		} else if (key.compareTo(getKey()) < 0) {
			return getLeft().get(key);
		} else {
			return getRight().get(key);
		}
	}
	
	public void remove(K key) {
		if (isEmpty()) {
			return;
		} else if (key.compareTo(getKey()) < 0) {
			getLeft().remove(key);
		} else if (key.compareTo(getKey()) > 0) {
			getRight().remove(key);
		} else if (getLeft().isEmpty()) {
			setRoot(getRight().root);
		} else if (getRight().isEmpty()) {
			setRoot(getLeft().root);
		} else {
			Node n = root.right.removeMin();
			root.key = n.key;
			root.value = n.value;
		}
	}
	
	private Node removeMin() {
		if (root.left.root == null) {
			Node n = root;
			root = root.right.root;
			return n;
		} else {
			return root.left.removeMin();
		}
	}
	
	private String toString2() {
		if (root == null) {
			return "";
		}
		String s = root.key + "->" + root.value + "\n";
		return s + root.left.toString2() + root.right.toString2();
	}
	
	public String toString() {
		return "{\n" + toString2() + "}";
	}

	private void print(int k, boolean printEmpty) {
		if (isEmpty() && !printEmpty) {
			return;
		}
		for(int i = 0; i < k; ++i) {
			System.out.print(" ");
		}
		if (isEmpty()) {
			System.out.println("-");
		} else {
			System.out.println(getKey());
			printEmpty = !getLeft().isEmpty() || !getRight().isEmpty();
			getLeft().print(k+1, printEmpty);
			getRight().print(k+1, printEmpty);
		}
	}
	
	public void print() {
		print(0, true);
	}
	
	public BinarySearchTree<K,V> createNewTree() {
		return new BinarySearchTree<K,V>();
	}
	
	public Node createNewNode(K key, V value) {
		return new Node(key, value);
	}
	
	public boolean isEmpty() {
		return root == null;
	}

	public Node getRoot() {
		return root;
	}
	
	public void setRoot(Node node) {
		root = node;
	}

	public K getKey() {
		return root.key;
	}
	
	public void setKey(K key) {
		root.key = key;
	}
	
	public V getValue() {
		return root.value;
	}
	
	public void setValue(V value) {
		root.value = value;
	}
	
	public BinarySearchTree<K,V> getLeft() {
		return root.left;
	}
	
	public void setLeft(BinarySearchTree<K,V> t) {
		root.left.root = t.root;
	}
	
	public BinarySearchTree<K,V> getRight() {
		return root.right;
	}
	
	public void setRight(BinarySearchTree<K,V> t) {
		root.right.root = t.root;
	}
	
}
