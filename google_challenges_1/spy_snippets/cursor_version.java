/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		String document = "a f f f d a a f d f a d d c a c";
		String[] searchTerms =  new String[] {"a", "c", "d"};
		//"d c a"
		/*String document = "many google employees can program";
		String[] searchTerms = new String[] {"google", "program"};
		//"google employees can program"*/
		
		System.out.println(answer(document, searchTerms));
	}
	
	public static String answer(String document, String[] searchTerms) { 
		HashMap<String, Integer> occurrences = new HashMap<String, Integer>();
		for(String st : searchTerms)
			occurrences.put(st,0);
		
		String[] words = document.split(" ");
		int begSnippet = 0;
		int endSnippet = 0;
		int snippetLen = Integer.MAX_VALUE;
		
		int lowerCursor = -1; 
		int upperCursor = -1;
		int currSnippetMissingWords = occurrences.size();
		int currSnippetLen = 0;
		
		int totOrder = 0;
		while(true){ //review ending validation
			/*UPPER CURSOR*/
			while(currSnippetMissingWords > 0 && upperCursor < words.length){
				upperCursor++;
				Integer occurr = occurrences.get(words[upperCursor]);

				if(occurr != null){   //relevant word only
					//System.out.println(totOrder + "- UP: "+ occurr);
					//totOrder++;
					
					occurr++;
					occurrences.put(words[upperCursor], occurr);
					if(occurr == 1)
						currSnippetMissingWords--;
				}
				System.out.println("UC: "+upperCursor+ " w:"+words[upperCursor] + " accu:"+occurr);				
			}
			//calculate range
			//if(currSnippetMissingWords == 0){
				currSnippetLen = upperCursor - lowerCursor;
				if(currSnippetLen < snippetLen){
					begSnippet = lowerCursor;
					endSnippet = upperCursor;
					snippetLen = currSnippetLen;
				}
			//}	
			System.out.println("begSnippet: "+begSnippet+ " endSnippet:"+endSnippet + " snippetLen:"+snippetLen);						
			/*LOWER CURSOR*/
			while(currSnippetMissingWords == 0){ 		// && lowerCursor < upperCursor
				lowerCursor++;
				Integer occurr = occurrences.get(words[lowerCursor]);

				if(occurr != null){   //relevant word only
					//System.out.println(totOrder + "- LOW: "+ occurr);
					//totOrder++;
					
					occurr--;
					occurrences.put(words[lowerCursor], occurr);
					if(occurr == 0)
						currSnippetMissingWords++;
				}
				System.out.println("LC: "+lowerCursor+ " w:"+words[lowerCursor] + " accu:"+occurr);				
			}
			
			//calculate range again
			//if(currSnippetMissingWords == 0){
				currSnippetLen = upperCursor - lowerCursor;
				if(currSnippetLen < snippetLen){
					begSnippet = lowerCursor;
					endSnippet = upperCursor;
					snippetLen = currSnippetLen;
				}		
			//}
			System.out.println("begSnippet: "+begSnippet+ " endSnippet:"+endSnippet + " snippetLen:"+snippetLen);	
			
			if(upperCursor >= words.length && lowerCursor >= words.length - occurrences.size()) //break if cursors reach max values 
				break;
			
		}
				
		String snippet = "";
		for(int i = begSnippet; i < endSnippet + 1; i++)
			snippet += words[i] + " ";

        return snippet.trim();			
    }	
}