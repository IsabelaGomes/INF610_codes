import java.io.BufferedReader;
import java.io.FileReader;

/*
 * The program "FindWords" reads a text file and prints its characters
 * on the screen. Modify the program so that it will print each word of the
 * text, preceded by the number of the line it occurs. A "word" is composed
 * only by letters. Each word must be printed using only lower-case letters.
 * Use the function "printWord" to print the lines and the words found.
 * 
 * Find below an example of the output expected by the modified program, when
 * executed using the file "input.txt" as input:
 
1 the
1 art
1 of
1 losing
1 isn
1 t
1 hard
1 to
1 master
2 so
2 many
2 things
... 
 */

public class FindWords {
	
	static void printWord(String s, int line) {
		System.out.println(line + " " + s);
	}
		
	public static void main(String[] args)  throws Exception {
		BufferedReader f = new BufferedReader(new FileReader("input.txt"));
		int c = f.read();
		String k = "";
		int linha = 1;
		boolean ew = false;
		while (true) {
			if (c == -1) {
				printWord (k,linha);
				break;
			}
			if (c>=65 && c<=90) {
				c+=32;
			}
			if (c<97 || c>122) {
				ew = true;
				if (c == '\n') {
					printWord (k,linha);
					linha++;
					k = "";
					ew = false;
				}
			}
			else {
				if (ew) {
					printWord (k,linha);
					k = "";
					ew = false;
				}
				k+= (char)c; 
			}
			c = f.read();
		}
		
		f.close();
	}

}

