import java.util.Scanner;
public class OddEven 
{
    int a[];
    int m;

    //Parametrized constructor
    OddEven(int mm)
    {
        m=mm;
        a=new int[m];
    }

    //input the elements
    void fillarray()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("input the number of elements");
        for(int i=0;i<m;i++)
        {
            a[i]=sc.nextInt();
        }
    }

    //arrange the elements
    OddEven arrange(OddEven P,OddEven Q)
    {
       int c=0;
       OddEven R=new OddEven(2*P.m);
       for (int i = 0; i < P.m; i++)
       {
        if(P.a[i]%2!=0)
        {
            R.a[c]=P.a[i];
            c++;
        }
       }
       for(int i=0;i<P.m;i++)
       {
        if(P.a[i]%2==0)
        {
            R.a[c]=P.a[i];
            c++;
        }
       }
       for(int i=0;i<P.m;i++)
       {
        if(Q.a[i]%2==0)
        {
            R.a[c]=Q.a[i];
            c++;
        }
       }
       return R; 
    }

    //print the array
    void display()
    {
        for (int i = 0; i < m; i++)
        {
            System.out.println(a[i]+" ");
        }
    }

    //main
    public static void main(String[] args)
    {
       Scanner sc=new Scanner(System.in);
       System.out.println("Input the number of elements in the array");
       int m=sc.nextInt();
       OddEven A=new OddEven(m);
       OddEven B=new OddEven(m);
       OddEven C=new OddEven(2*m);
       A.fillarray();
       B.fillarray();
       C=C.arrange(A, B);
       System.out.println("Arranged Array: ");
       C.display();
    }
}
