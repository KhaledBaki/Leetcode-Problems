/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

 // Imports
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public boolean hasCycle(ListNode head) {
        List<ListNode> list = new ArrayList<ListNode>();
        ListNode cursor = head;

        while(cursor != null){
            if(list.contains(cursor)){
                return true;
            }

            list.add(cursor); 
            cursor = cursor.next;
        }
        return false;
    }
}
