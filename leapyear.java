public class leapyear
{

    public static void main(String[] args)
     {
    
      int year=2019;
        if(year%4==0)
        {
            System.out.println("leap year");

            if(year%100==0)
            {
                System.out.println("not a year");
                if(year%400==0)
                {
                    System.out.println("leap year");
                }
                else 
                {
                    System.out.println("not a leap year");
                }
            }
            else
            {
               System.out.println("leap year");
            }
        }
        else
        {
        System.out.println("not a leap year");
        }
    }
}
