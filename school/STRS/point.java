import java.util.*;

import javax.swing.plaf.synth.SynthEditorPaneUI;
public class point
{
    int a[];
    point()
    {
        a=new int[2]; 
    }
    void readpoint()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the value");
        a[0]=sc.nextInt();
        a[1]=sc.nextInt();
    }
    point midPoint(point A)
    {
        point C=new point();
        C.a[0]=(A.a[0]+a[0])/2;
        C.a[1]=(A.a[1]+a[1])/2;
        return C;
    }
    void display()
    {
        System.out.println("The x value is "+a[0]);
        System.out.println("The y value is "+a[1]);
    }
    public static void main(String[] args) {
        point A=new point();
        A.readpoint();
        point B=new point();
        B.readpoint();
        point C=new point();
        C=B.midPoint(A);
        C.display();
    }
}