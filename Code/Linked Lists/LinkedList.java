
import java.util.Scanner;

class Node{
    int data;
    Node next;
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}

public class LinkedList{
    Node head = null;
    public LinkedList(){}
    void insert(int data){
        Node newNode = new Node(data);
        if(this.head == null)
            this.head = newNode;
        else{
            Node temp = this.head;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }
    void printList(){
        Node temp = this.head;
        while(temp != null){
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("null");
        System.out.println("");
    }
    public static void main(String[] args) {
        LinkedList l1 = new LinkedList();
        Scanner sc = new Scanner(System.in);
        while (true) { 
            System.out.println("Enter data to append or -1 to \"exit\": ");
            int data = sc .nextInt();
            if(data == -1) break;
            l1.insert(data);
            l1.printList();
        }
    }
}