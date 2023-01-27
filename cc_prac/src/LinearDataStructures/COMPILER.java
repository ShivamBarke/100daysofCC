package LinearDataStructures;
//https://www.codechef.com/problems/COMPILER
import java.util.*;
import java.lang.*;
import java.io.*;
public class COMPILER {

    public static void main (String[] args) throws java.lang.Exception
	{    
		try {
		    Scanner input = new Scanner(System.in);
	        int T = input.nextInt();
            input.nextLine();
            for(int x=1;x<=T;x++){
                String s=input.nextLine();
                int count=0;
                int index = 0;
                for (int i=0;i<s.length();i++) {   
                    // <<>
                    // ><
                    // <<<>
                    // <>><                   
                    
                    if (s.charAt(i) == '<') {
                        count++;
                    } 
                    else {
                        count--;
                        
                    }
                    if(count<0) {
                        break;
                    }
                    
                    if(count==0) {
                        index= i+1;   
                    }                    
                       
                }
                System.out.println(index);
	        }
	        input.close();
		}
	    catch(Exception e) {
	        e.printStackTrace();
	    }
    }
}
