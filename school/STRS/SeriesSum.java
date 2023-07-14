import java.util.*;
public class SeriesSum
{
    int X;
    int N;
    double sum;

    SeriesSum(int xx,int nn)
    {
        X=xx;
        N=nn;
    }
    
    double CalFact(int m)
    {
        if(m<0)
            return 1;
        else
            return(m*(CalFact(m-1)));
    }
    
    double CalPower(int x,int y)
    {
        if(y<0)
            return 1;
        else
            return(CalPower(x*X, y-1));
    }

    void CaLSum()
    {
        sum+=CalPower(X,N)/CalFact(N-1);
        N=N-2;
        if(N-1>0)
            CaLSum();
    }

    void display()
    {
        System.out.print("The Sum of the variable is:"+sum);
    }

    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Input the value of x and n");
        int x=sc.nextInt();
        int n=sc.nextInt();
        SeriesSum obj=new SeriesSum(x,n);
        obj.CaLSum();
        obj.display();
    }
}
