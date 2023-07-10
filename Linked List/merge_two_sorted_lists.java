public class merge_two_sorted_lists {
    
}


//Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list3 = new ListNode();
        ListNode t1 = list1;
        ListNode t2 = list2;
        ListNode t3 = list3;

        while(t1!=null && t2!=null){
            if(t1.val<t2.val){
                t3.next = new ListNode(t1.val);
                t1 = t1.next;
            }
            else{
                t3.next = new ListNode(t2.val);
                t2 = t2.next;
            }
            t3 = t3.next;
        }
        if(t1!=null){
            t3.next = t1;
        }
        if(t2!=null){
            t3.next = t2;
        }

        return list3.next;
    }
}