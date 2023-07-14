import java.util.*;
class hello
{
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("input you name");
            String name=sc.next();
            String newwrd="";
            for(int i=name.length()-1;i>=0;i--)
            {
                newwrd += name.charAt(i);
            }
            System.out.println(newwrd);
        }
    }
}