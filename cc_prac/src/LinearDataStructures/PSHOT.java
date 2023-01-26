package LinearDataStructures;
import java.util.*;
import java.lang.*;
import java.io.*;
public class PSHOT {
    public static void main (String[] args) throws java.lang.Exception
	{
		try {
		    Scanner input = new Scanner(System.in);
	        int T = input.nextInt();
            for(int x=1;x<=T;x++){
                int n = input.nextInt();
                String s = input.next();
                
                int g_a = 0;
                int g_b = 0;
                int rem_a = n;
                int rem_b = n;
                int flag = 1;
                for(int i=0;i<2*n;i++){
                    if(i%2==0){
                        //A's shot
                        if(s.charAt(i)=='1'){
                        g_a++;
                    }
                        rem_a--;
                    } else {
                        //B's shot
                        if(s.charAt(i)=='1'){
                        g_b++;
                    }
                        rem_b--;
                    }
                    if (g_a-g_b> rem_b) {
                        System.out.println(i+1);
                        flag = 0;
                        break;
                    } else if (g_b-g_a>rem_a) {
                        System.out.println(i+1);
                        flag = 0;
                        break;
                    }
                }
                if (flag==1) {
                    System.out.println(2*n);
                }
            
	    }
	    input.close();
		}
	    catch(Exception e) {
	        e.printStackTrace();
	    }
	}
}
