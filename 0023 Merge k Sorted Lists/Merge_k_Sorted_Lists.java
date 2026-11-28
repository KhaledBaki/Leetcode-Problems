class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }
        for(int i = 1; i < lists.length; i++){
            ListNode sorted = sort(lists[0], lists[i]);
            lists[0] = sorted;
        }
        return lists[0];
    }

    private ListNode sort(ListNode list1, ListNode list2){
        ListNode newList = new ListNode();
        ListNode newListCursor = newList;

        ListNode c1 = list1;
        ListNode c2 = list2;

        while(c1 != null && c2 != null){
            if(c1.val < c2.val){
                newListCursor.next = new ListNode(c1.val);
                newListCursor = newListCursor.next;
                c1 = c1.next;
            }
            else if(c1.val > c2.val){
                newListCursor.next = new ListNode(c2.val);
                newListCursor = newListCursor.next;
                c2 = c2.next;
            }
            else{
                newListCursor.next = new ListNode(c1.val);
                newListCursor = newListCursor.next;

                newListCursor.next = new ListNode(c2.val);
                newListCursor = newListCursor.next;
                
                c1 = c1.next;
                c2 = c2.next;
            } 
        }

        if(c1 != null && c2 != null){
            return newList.next;
        }

        if(c1 == null){
            while(c2 != null){
                newListCursor.next = new ListNode(c2.val);
                newListCursor = newListCursor.next;
                c2 = c2.next;
            }
            return newList.next;
        }

        // c2 == null
        while(c1 != null){
            newListCursor.next = new ListNode(c1.val);
            newListCursor = newListCursor.next;
            c1 = c1.next;
        }
        return newList.next;
    }
}
