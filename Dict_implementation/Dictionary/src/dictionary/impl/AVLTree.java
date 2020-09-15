package dictionary.impl;

import dictionary.interfaces.Dictionary;

public class AVLTree <K extends Comparable<K>, V>
extends BinarySearchTree<K, V>
implements Dictionary<K, V> {

	private class Node extends BinarySearchTree<K,V>.Node {
		private int height;
		public Node(K key, V value) {
			super(key, value);
			height = 1;
		}
	}
	
	public AVLTree<K,V> createNewTree() {
		return new AVLTree<K,V>();
	}
	
	public Node createNewNode(K key, V value) {
		return new Node(key, value);
	}
	
	public Node getRoot() {
		return (Node) super.getRoot();
	}

	public int getHeight() {
		if (isEmpty()) {
			return 0;
		}
		return getRoot().height;
	}
	
	public void setHeight(int height) {
		getRoot().height = height;
	}
	
	AVLTree<K,V> copy() {
		AVLTree<K,V> aux = new AVLTree<K,V>();
		aux.setRoot(getRoot());
		return aux;
	}
	
	public void put(K key, V value) {
		if (isEmpty()) {
			setRoot(createNewNode(key, value));
		} else if (key.compareTo(getKey()) < 0) {
			getLeft().put(key, value);
		} else if (key.compareTo(getKey()) > 0) {
			getRight().put(key, value);
		} else {
			setValue(value);
		}
		
		setHeight(1 + max(getLeft().getHeight(), getRight().getHeight()));
		
		int balance = getLeft().getHeight() - getRight().getHeight();
		if (balance > 1 && key.compareTo(getLeft().getKey()) < 0) {
			// Left Left Case
			rightRotate();
		} else if (balance < -1 && key.compareTo(getRight().getKey()) > 0) {
			// Right Right Case
			leftRotate();
		} else if (balance > 1 && key.compareTo(getLeft().getKey()) > 0) {
			// Left Right Case
			getLeft().leftRotate();
			rightRotate();
		} else if (balance < -1 && key.compareTo(getRight().getKey()) < 0) {
			// Right Left Case
			getRight().rightRotate();
			leftRotate();
		}
	}
	
	private void rightRotate() {
		AVLTree<K,V> x = getLeft().copy();
		AVLTree<K,V> T2 = x.getRight().copy();
        x.setRight(copy());
        setLeft(T2);
        setHeight(max(getLeft().getHeight(), getRight().getHeight()) + 1);
        x.setHeight(max(x.getLeft().getHeight(), x.getRight().getHeight()) + 1);
        setRoot(x.getRoot());
    }
	 
    private void leftRotate() {
    	AVLTree<K,V> y = getRight().copy();
    	AVLTree<K,V> T2 = y.getLeft().copy();
        y.setLeft(copy());
        setRight(T2);
        setHeight(max(getLeft().getHeight(), getRight().getHeight()) + 1);
        y.setHeight(max(y.getLeft().getHeight(), y.getRight().getHeight()) + 1);
        setRoot(y.getRoot());
    }
    		
	public AVLTree<K,V> getLeft() {
		return (AVLTree<K,V>) super.getLeft();
	}
	
	public AVLTree<K,V> getRight() {
		return (AVLTree<K,V>) super.getRight();
	}
	
	private static int max(int i1, int i2) {
		return (i1 > i2) ? i1 : i2;
	}

}
