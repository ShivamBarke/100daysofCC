/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
/* Name of the class has to be "Main" only if the class is public. */
class STFOOD
{
	public static void main (String[] args) throws java.lang.Exception
	{
		try {
		    Scanner input = new Scanner(System.in);
	        int T = input.nextInt();
            for(int i=1;i<=T;i++){
                int n = input.nextInt();
                int[] profit = new int[101];
                for(int x=1;x<=n;x++){
                    int s = input.nextInt();
                    int p = input.nextInt();
                    int v = input.nextInt();
                    int pro = (p/(s+1))*v;
                    profit[x] = pro;
                }
            System.out.println(Arrays.stream(profit).max().getAsInt());
	    }
	    input.close();
		}
	    catch(Exception e) {
	        e.printStackTrace();
	    }
	}
}
