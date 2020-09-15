package dictionary.impl;

import dictionary.interfaces.Dictionary;

public class BTree <K extends Comparable<K>, V>
implements Dictionary<K, V> {

	private Node root; // the B-tree is a pointer to the root node
	private int D;     // the order is D*2+1
	
	private class Item {
		private K key;
		private V value;
		Node child;
		public Item(K key, V value) {
			this.key = key;
			this.value = value;
		}
	}
	
	private class Node {
		private int m;          // number of keys in the node
		Node first;             // points to the first child
		private Object[] items; // array of Itens (key+value+pointer)
		public Node() {
			items = new Object[D*2+1];
			m = 0;
		}
		public Item getItem(int i) {
			return (Item) items[i];
		}
	}
	
	public BTree(int d) {
		D = d;
		root = null;
	}

	public void put(K key, V value) {
		Item it = put(root, key, value);
		if (it != null) {
			Node node = new Node();
			node.first = root;
			node.items[0] = it;
			node.m = 1;
			root = node;
		}
	}
	
	private Item put(Node node, K key, V value) {
		if (node == null) {
			return new Item(key, value);
		}
		int i = 0;
		while (i < node.m) {
			int c = key.compareTo(node.getItem(i).key);
			if (c == 0) {
				node.getItem(i).value = value;
				return null;
			} else if (c < 0) {
				break;
			}
			++i;
		}
		Node next = node.first;
		if (i > 0) {
			next = node.getItem(i-1).child;
		}
		Item it = put(next, key, value);
		if (it != null) {
			for(int k = node.m; k > i; --k) {
				node.items[k] = node.items[k-1];
			}
			node.items[i] = it;
			node.m++;
			if (node.m <= 2*D) {
				return null;
			} else {
				Node node2 = new Node();
				for(int k = D+1; k <= 2*D; ++k) {
					node2.items[k-D-1] = node.items[k];
				}
				it = node.getItem(D);
				node2.first = it.child;
				it.child = node2;
				node2.m = D;
				node.m = D;
			}
		}
		return it;
	}

	public V get(K key) {
		return get(root, key);
	}
	
	private V get(Node node, K key) {
		if (node == null) {
			return null;
		}
		int i = 0;
		while (i < node.m) {
			int c = key.compareTo(node.getItem(i).key);
			if (c == 0) {
				return node.getItem(i).value;
			} else if (c < 0) {
				if (i == 0) {
					return get(node.first, key);
				} else {
					return get(node.getItem(i-1).child, key);
				}
			}
			++i;
		}
		return get(node.getItem(node.m - 1).child, key);
	}

	boolean isLeaf(Node node) {
		return node.first == null;
	}
	
	public void remove(K key) {
		remove(root, key);
		if (root.m == 0) {
			root = root.first;
		}
	}
	
	private boolean remove(Node node, K key) {
		if (node == null) {
			return false;
		}
		int i = 0;
		boolean b;
		while (i < node.m) {
			int c = key.compareTo(node.getItem(i).key);
			if (c == 0) { // found the key in the current node
				if (isLeaf(node)) {
					for(int j = i; j < node.m-1; ++j) {
						node.items[j] = node.items[j+1];
					}
					node.m--;
				} else {
					b = removeMin(node.getItem(i).child, node, i);
					if (b) {
						rebalance(node, i+1);
					}
				}
				return node.m < D;					
			} else if (c < 0) {
				break;
			}
			++i;
		}
		Node node2;
		if (i == 0) { node2 = node.first; }
		else { node2 = node.getItem(i-1).child; }
		b = remove(node2, key);
		if (b) {
			rebalance(node, i);
		}
		return node.m < D;
	}
	
	boolean removeMin(Node node, Node nodeMin, int posMin) {
		if (isLeaf(node)) {
			nodeMin.getItem(posMin).key = node.getItem(0).key;
			nodeMin.getItem(posMin).value = node.getItem(0).value;
			for(int j = 0; j < node.m-1; ++j) {
				node.items[j] = node.items[j+1];
			}
			node.m--;
			return node.m < D;
		}
		boolean b = removeMin(node.first, nodeMin, posMin);
		if (b) {
			rebalance(node, 0);
		}
		return node.m < D;
	}

	private void rebalance(Node node, int i) {
		Node before, node2, after;
		if (i == 0) {
			before = null;
		} else if (i == 1) {
			before = node.first;
		} else {
			before = node.getItem(i-2).child;
		}
		if (i == 0) {
			node2 = node.first;
		} else {
			node2 = node.getItem(i-1).child;
		}
		if (i == node.m) {
			after = null;
		} else {
			after = node.getItem(i).child;
		}
		assert node2.m < D;
		if (before != null && before.m > D) {
			for(int j = node2.m; j > 0; --j) {
				node2.items[j] = node2.items[j-1];
			}
			node.getItem(i-1).child = node2.first;
			node2.items[0] = node.items[i-1];
			node2.first = before.getItem(before.m-1).child;
			node2.m = D;
			before.getItem(before.m-1).child = node2;
			node.items[i-1] = before.items[before.m-1];
			before.m--;
		} else if (after != null && after.m > D) {
			node.getItem(i).child = after.first;
			node2.items[node2.m] = node.items[i];
			node2.m = D;
			after.first = after.getItem(0).child;
			after.getItem(0).child = after;
			node.items[i] = after.items[0];
			for(int j = 0; j < after.m-1; ++j) {
				after.items[j] = after.items[j+1];
			}
			after.m--;
		} else if (before != null) {
			node.getItem(i-1).child = node2.first;
			before.items[D] = node.items[i-1];
			for(int j = 0; j < node2.m; ++j) {
				before.items[j+D+1] = node2.items[j];
			}
			before.m = 2*D;
			for(int j = i-1; j < node.m-1; ++j) {
				node.items[j] = node.items[j+1];
			}
			node.m--;
		} else {
			assert after != null;
			node.getItem(i).child = after.first;
			node2.items[D-1] = node.items[i];
			for(int j = 0; j < after.m; ++j) {
				node2.items[j+D] = after.items[j];
			}
			node2.m = 2*D;
			for(int j = i; j < node.m-1; ++j) {
				node.items[j] = node.items[j+1];
			}
			node.m--;			
		}
	}
	
	private void print(Node node, int k) {
		if (node == null) {
			return;
		}
		print(node.first, k+1);
		for (int j = 0; j < node.m; ++j) {
			for(int i = 0; i < k; ++i) {
				System.out.print(" ");
			}
			System.out.println(node.getItem(j).key);
			print(node.getItem(j).child, k+1);
		}
	}
	
	public void print() {
		print(root, 0);
	}
	
	private String toString(Node node) {
		if (node == null) {
			return "";
		}
		String s = "";
		s += toString(node.first);
		for(int i = 0; i < node.m; ++i) {
			s += node.getItem(i).key + "->" + node.getItem(i).value + "\n";
			s += toString(node.getItem(i).child);
		}
		return s;
	}
	
	public String toString() {
		return "{\n" + toString(root) + "}";
	}


	public static void main(String args[]) {
		BTree d = new BTree<Integer, String>(2);
		d.put(1, "One");
		d.put(9, "nine");
		d.put(5, "five");
		d.put(3, "three");
		d.put(1, "one");
		d.put(4, "four");
		d.put(6, "six");
		d.put(8, "eight");
		d.put(7, "seven");
		d.print();
		System.out.println(d.get(6));
		System.out.println(d.get(7));
		System.out.println(d.get(8));
		System.out.println(d.get(9));
	}
	
}