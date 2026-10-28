class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode actual = head;
        ListNode delayed = head;

        for(int i = 0; i <= n; i++){
            if(delayed == null){
                return head.next;
            }
            delayed = delayed.next;
        }

        while (delayed != null){
            actual = actual.next;
            delayed = delayed.next;
        }
        if(actual.next != null)
            actual.next = actual.next.next;
        return head;
    }
}
