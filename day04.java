import java.util.List;
import java.util.Hashtable;
import java.nio.file.Files;
import java.nio.file.Paths;

// Day 04
// Part 1: Find all lines that contain no duplicates
// Part 2: Find all lines that contain no two words that are anagrams

class day04 {

    public static void main(String[] args) {
	List<String> lines;
	try {
	    lines = Files.readAllLines(Paths.get("./day04.data"));
	} catch(Exception e) {
	    System.out.println("Couldn't read file: " +e);
	    return;
	}	
	System.out.println("Part 1: " +solvePart(1, lines));
	System.out.println("Part 2: " +solvePart(2, lines));
    }

    public static int solvePart(int part, List<String> lines) {
	int count = 0;
	boolean bbreak = false;
	for (String line : lines) {
	    bbreak = false;
	    String[] words = line.split(" ");
	    for (int i=0; i < words.length-1;i++) {
		for (int j=i+1; j < words.length;j++) {
		    if (part == 1 && words[i].equals(words[j])) {
			bbreak = true;
		    } else if (part == 2 && isAnagram(words[i], words[j])) {
			bbreak = true;
		    }
		    if (bbreak) break;
		}
		if (bbreak) break;
	    }
	    if (!bbreak) count++;
	}
	return count;
    }

    public static Hashtable<Character, Integer> countChars(String s) {
	Hashtable<Character, Integer> count = new Hashtable<>();
	for (int i=0; i<s.length(); i++) {
	    char c = s.charAt(i);
	    if (count.get(c) == null) count.put(c, 1);
	    else count.put(c, count.get(c));
	}
	return count;
    }

    // Two words are anagrams iff they contain the same amount of characters
    public static boolean isAnagram(String a, String b) {
	return countChars(a).equals(countChars(b));
    }
}
