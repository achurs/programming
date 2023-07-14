import java.util.*;
public class check 
{
    String wrd;
    int len;
    check()
    {
        wrd="";
        len=0;
    }
    void accept_word()
    {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Input the word");
            wrd=sc.next();
        }
    }
    Boolean Palindrome()
    {
        boolean falg=false;
        len=wrd.length();
        String revwrd="";
        for(int i=len-1;i>=0;i--)
        {
            revwrd+=wrd.charAt(i);
        }
        if(wrd.equalsIgnoreCase(revwrd))
        falg=true;
        return falg;
    }
    void Display(boolean value)
    {
        if(value)
        {
        System.out.println("The word is palindrome");
        }
        else
        {
        System.out.println("the Word is not palindrome");
        }
    }
    public static void main(String[] args)
    {
        check obj=new check();
        obj.accept_word();
        boolean value=obj.Palindrome();
        obj.Display(value);
    }   
}
