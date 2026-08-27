class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		
        ListNode cursorOne = list1;
        ListNode cursorTwo = list2;
		ListNode mergerdList;
		
        // same
        if(cursorOne.val == cursorTwo.val){
			mergerdList = new ListNode(cursorOne.val);
			
			ListNode mergerdListCursor = mergerdList;
            mergerdListCursor.next = new ListNode(cursorTwo.val);
			
			cursorOne = cursorOne.next;
			cursorTwo = cursorTwo.next;
		}

        // less than
		else if(cursorOne.val < cursorTwo.val){
			mergerdList = new ListNode(cursorOne.val);
			cursorOne = cursorOne.next;
		}

        // else case
		else{
			mergerdList = new ListNode(cursorTwo.val);
			cursorTwo = cursorTwo.next;
		}
		
		while(cursorOne != null || cursorTwo != null){
			if(cursorOne == null){
				mergerdListCursor.next = new ListNode(cursorTwo.val);
				cursorTwo = cursorTwo.next;
				mergerdListCursor = mergerdListCursor.next;
			}
			else if(cursorTwo == null){
				mergerdListCursor.next = new ListNode(cursorOne.val);
				cursorOne = cursorOne.next;
				mergerdListCursor = mergerdListCursor.next;
			}
			else if(cursorOne.val == cursorTwo.val){
				mergerdListCursor.next = new ListNode(cursorOne.val);
				cursorOne = cursorOne.next;
				cursorTwo = cursorTwo.next;
				mergerdListCursor = mergerdListCursor.next;
			}

			// less than
			else if(cursorOne.val < cursorTwo.val){
				mergerdListCursor.next = new ListNode(cursorOne.val);
				cursorOne = cursorOne.next;
				mergerdListCursor = mergerdListCursor.next;
			}

			// else case
			else{
				mergerdListCursor.next = new ListNode(cursorTwo.val);
				cursorTwo = cursorTwo.next;
				mergerdListCursor = mergerdListCursor.next;
			}
		}
		return mergerdList;
    }
}