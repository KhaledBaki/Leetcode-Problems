class Solution {
    public ListNode middleNode(ListNode head) {
        int listSize = 0;

        ListNode current = head;
        while(current != null){
            listSize++;
            current = current.next;
        }

        ListNode curr = head;
        for(int i = 0; i < listSize / 2; i++){
            curr = curr.next;
        }
        return curr;
    }
}
