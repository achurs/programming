public class niru {
    public static void main(String[] args) {
        add(1, 2, 3, 4, 5,6,7,8,9,10);
    }
    public static void add(int... arr) {
        int sum = 0;
        System.out.println(arr[0]);
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        System.out.println(sum);
    }
}