package tests;

import java.util.Calendar;
import java.util.Random;

import dictionary.impl.AVLTree;
import dictionary.impl.BTree;
import dictionary.impl.BinarySearchTree;
import dictionary.interfaces.Dictionary;

public class TestRandom {

	static Random randomGenerator;
		
	static void testRandom(Dictionary<Integer,String> d) {
		
	    int num = 1000000;
	    int range = 1000000000;
	    
	    
	    for (int idx = 1; idx <= num; ++idx){
	    	int r = randomGenerator.nextInt(range);
	    	d.put(r, "");
	    }

	    int found = 0;
	    for (int idx = 1; idx <= num; ++idx){
	    	int r = randomGenerator.nextInt(range);
	    	if (d.get(r) != null) {
	    		++found;
	    	}
	    }
	    
	    System.out.println("Found " + found + " keys from " + num + " random keys");

	}

	
	public static void main(String[] args) {
		
		long k = Calendar.getInstance().getTime().getTime();
		System.out.println("Seed = " + k);

		randomGenerator = new Random(k);
		Dictionary<Integer,String> d1 = new BinarySearchTree<Integer,String>();
		testRandom(d1);

		randomGenerator = new Random(k);
		Dictionary<Integer,String> d2 = new AVLTree<Integer,String>();
		testRandom(d2);

		randomGenerator = new Random(k);
		Dictionary<Integer,String> d3 = new BTree<Integer,String>(10);
		testRandom(d3);

	}

}
