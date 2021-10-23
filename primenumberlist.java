import java.util.Scanner;
public class primenumberlist 
{

    public static void main (String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the no");
        int no=sc.nextInt();
        
        for (int no=1;no<=100;no++)
        {
            int temp=0;
            for(int j=2;j<=no-1;j++)
            {
                if(no%j==0)
                {
                    temp=temp+1;
                }
                if(temp==0)
                {
                    System.out.println(no);   
                }
             
            }
        }
    }
    
}
