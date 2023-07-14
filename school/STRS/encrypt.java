import java.util.*;
public class encrypt 
{
    String wrd;
    int len;
    String nwword;

    encrypt()
    {
        wrd="";
        len=0;
        nwword="";
    }
    void AcceptWord()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("input a word");
        wrd=sc.nextLine();
        len=wrd.length();
    }
    void freq()
    {
        int vcnt=0;
        int ccout=0;
        for(int i=0;i<len;i++)
        {
            char ch=wrd.charAt(i);
            if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
            vcnt++;
            else
            ccout++;
        }
        System.out.println("The number of vovels:"+vcnt);
        System.out.println("the number of consonut:"+ccout);
    }
    void nextword()
    {
        for(int i=0;i<len;i++)
        {
            char ch=wrd.charAt(i);
            if(ch=='a')
            ch='e';
            else if(ch=='e')
            ch='i';
            else if(ch=='i')
            ch='o';
            else if(ch=='o')
            ch='u';
            else if(ch=='u')
            ch='a';

            nwword+=ch;
        }
    }
    void display()
    {
        System.out.println("the original word:"+wrd);
        System.out.println("The new word:"+nwword);
    }
    public static void main(String[] args)
    {
        encrypt obj=new encrypt();
        obj.AcceptWord();
        obj.freq();
        obj.nextword();
        obj.display();
    }    
}
