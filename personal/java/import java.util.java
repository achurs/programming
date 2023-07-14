import java.util.ArrayList;
import java.util.List;

class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public double getPrice() { Main {
        return price;
    }
}

class ShoppingCart {
    private List<Product> items;

    public ShoppingCart() {
        items = new ArrayList<>();
    }

    public void addItem(Product product) {
        items.add(product);
    }

    public void removeItem(Product product) {
        items.remove(product);
    }

    public void displayItems() {
        System.out.println("Shopping Cart Items:");
        for (Product item : items) {
            System.out.println(item.getName() + " - $" + item.getPrice());
        }
    }

    public double calculateTotalPrice() {
        double total = 0.0;
        for (Product item : items) {
            total += item.getPrice();
        }
        return total;
    }
}

public class ShoppingApp {
    public static void main(String[] args) {
        // Create some sample products
        Product product1 = new Product("Product 1", 10.99);
        Product product2 = new Product("Product 2", 19.99);
        Product product3 = new Product("Product 3", 5.99);

        // Create a shopping cart
        ShoppingCart cart = new ShoppingCart();

        // Add products to the cart
        cart.addItem(product1);
        cart.addItem(product2);
        cart.addItem(product3);

        // Display cart items and total price
        cart.displayItems();
        System.out.println("Total Price: $" + cart.calculateTotalPrice());
    }
}
}
