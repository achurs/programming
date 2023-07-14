import java.util.*;
public class CountCapital
{
    String word;
    int LGTH;
    int Count;

    CountCapital()
    {
        word="";
        LGTH=0;
        Count=0;
    }
    void readWord()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Input a word");
        word=sc.nextLine();
        LGTH=word.length();
    }
    void countCap()
    {
        for(int i=0;i<LGTH;i++)
        {
            char ch=word.charAt(i);
            if(ch>='A'&&ch<='Z')
            {
                Count++;
            }
        }
    }
    void display()
    {
        System.out.println("The total number of capital letters are:"+Count);
    }
    public static void main(String[] args)
    {
        CountCapital obj=new CountCapital();
        obj.readWord();
        obj.countCap();
        obj.display();

    }    
}
