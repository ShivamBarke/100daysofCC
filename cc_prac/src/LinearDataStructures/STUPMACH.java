package LinearDataStructures;
import java.util.*;
import java.lang.*;
import java.io.*;
//https://www.codechef.com/problems/STUPMACH
public class STUPMACH {
    public static void main (String[] args) throws java.lang.Exception
	{
		try {
            Scanner input = new Scanner(System.in);
            int T = input.nextInt();
            for(int i=1;i<=T;i++){
                int n = input.nextInt();
                int[] S = new int[n];
                for(int x=0;x<n;x++){
                    S[x] = input.nextInt();
                }
                long total = S[0]; 
                for(int x=1;x<n;x++){
                    S[x] = Math.min(S[x], S[x-1]);
                    total = total + S[x];
                }
                
        
                System.out.println(total);
            
        }
        input.close();
        }
        catch(Exception e) {
            e.printStackTrace();
        }
	}
}

//partially correct for test cases causes TLE
// try {
//     Scanner input = new Scanner(System.in);
//     int T = input.nextInt();
//     for(int i=1;i<=T;i++){
//         int n = input.nextInt();
//         int[] S = new int[n];
//         for(int x=0;x<n;x++){
//             S[x] = input.nextInt();
//         }
//         int[] total = new int[n]; 
//         for(int x=0;x<n;x++){
//             int[] arr = Arrays.copyOfRange(S, 0, x + 1);
            
//             int min = Arrays.stream(arr).min().getAsInt();
//             total[x] = min;
//         }
        

//         System.out.println(Arrays.stream(total).sum());
    
// }
// input.close();
// }
// catch(Exception e) {
//     e.printStackTrace();
// }
//----------------------------------------------------------------
//partially correct for test cases causes TLE
// try {
//     Scanner input = new Scanner(System.in);
//     int T = input.nextInt();
//     for(int i=1;i<=T;i++){
//         int n = input.nextInt();
//         ArrayList<Integer> list = new ArrayList<Integer>();
//         List<Integer> total = new ArrayList<Integer>();
//         for (int x = 0; x < n; x++) {
//             int num = input.nextInt();
//             list.add(num);
//             List<Integer> arr = list.subList(0, x + 1);
//             int min = Collections.min(arr);
//             total.add(min);
//         }
//         int res = total.stream().mapToInt(Integer::intValue).sum();
        
//         System.out.println(res);
    
// }
// input.close();
// }
// catch(Exception e) {
//     e.printStackTrace();
// }