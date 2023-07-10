
//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        int carry = 0;
        while(l1!=null || l2!=null || carry==1){
            int l1_val = 0;
            if(l1!=null){
                l1_val = l1.val;
            }
            int l2_val = 0;
            if(l2!=null){
                l2_val = l2.val;
            }

            int val = l1_val + l2_val + carry;
            carry = val/10;
            val = val%10;

            ListNode newNode = new ListNode(val);
            cur.next = newNode;
            cur = cur.next;
            if(l1 != null){
                l1 = l1.next;
            }
            if(l2 != null){
                l2 = l2.next;
            }
        }
        return dummy.next;
    }
}