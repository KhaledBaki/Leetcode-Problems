/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		
        ListNode cursorOne = list1;
        ListNode cursorTwo = list2;
		ListNode mergerdList = new ListNode();
        ListNode mergedListCursor;
        
		
        // Null list edge cases
        if(cursorOne == null){
            return list2;
        }
        else if (cursorTwo == null){
            return list1;
        }

        // Case 1 EQUAL case
        if(cursorOne.val == cursorTwo.val){

			mergerdList = new ListNode(cursorOne.val);
            mergedListCursor = mergerdList;
            mergedListCursor.next = new ListNode(cursorTwo.val);
            
            mergedListCursor = mergedListCursor.next;
			cursorOne = cursorOne.next;
			cursorTwo = cursorTwo.next;
		}

        // Case 2 LESS than case
		else if(cursorOne.val < cursorTwo.val){
			mergerdList = new ListNode(cursorOne.val);
            mergedListCursor = mergerdList;
			cursorOne = cursorOne.next;
		}

        // Case 3 ELSE case
		else{
			mergerdList = new ListNode(cursorTwo.val);
            mergedListCursor = mergerdList;
			cursorTwo = cursorTwo.next;
		}
		
		while(cursorOne != null || cursorTwo != null){\

			if(cursorOne == null){
				mergedListCursor.next = new ListNode(cursorTwo.val);
				cursorTwo = cursorTwo.next;
				mergedListCursor = mergedListCursor.next;
			}

			else if(cursorTwo == null){
				mergedListCursor.next = new ListNode(cursorOne.val);
				cursorOne = cursorOne.next;
				mergedListCursor = mergedListCursor.next;
			}

			else if(cursorOne.val == cursorTwo.val){
				mergedListCursor.next = new ListNode(cursorOne.val);
                mergedListCursor = mergedListCursor.next;

                mergedListCursor.next = new ListNode(cursorOne.val);
                mergedListCursor = mergedListCursor.next;

				cursorOne = cursorOne.next;
				cursorTwo = cursorTwo.next;
			}

			else if(cursorOne.val < cursorTwo.val){
				mergedListCursor.next = new ListNode(cursorOne.val);
				cursorOne = cursorOne.next;
				mergedListCursor = mergedListCursor.next;
			}

			else{
				mergedListCursor.next = new ListNode(cursorTwo.val);
				cursorTwo = cursorTwo.next;
				mergedListCursor = mergedListCursor.next;
			}
		}
		return mergerdList;
    }
}
