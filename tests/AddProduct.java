// Add a product
// to the 'on-order' list
public class AddProduct {

    private int id;
    private char[] name;
    private int orderCode;

    public AddProduct(int id, char[] name, int orderCode) {
        this.id = id;
        this.name = name;
        this.orderCode = orderCode;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public char[] getName() {
        return name;
    }

    public void setName(char[] name) {
        this.name = name;
    }

    public int getOrderCode() {
        return orderCode;
    }

    public void setOrderCode(int orderCode) {
        this.orderCode = orderCode;
    }

}