package zero.fiftieth;

class ListNode{
    int val;
    ListNode next;
    ListNode(int val){
        this.val = val;
    }
}

public class Test92 {
    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);
        ListNode node5 = new ListNode(5);
        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;
        Test92 test92 = new Test92();
        ListNode re = test92.reverseBetween(node1,2,4);
        while(re != null){
            System.out.println(re.val+" ");
            re = re.next;
        }
    }
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode prev = dummyHead, cur = head;
        ListNode third = null;
        while( m > 1){
            prev = cur;
            cur = cur.next;
            m--;
            n--;
        }

        while(n > 1){
            third = cur.next;
            cur.next = third.next;
            third.next = prev.next;
            prev.next = third;
            n--;
        }
        return dummyHead.next;
    }
}
