/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Initialize two pointers
        ListNode* prev = NULL;
        ListNode* curr = head;

        // Iterate as long as the current pointer is not null
        while (curr) {
            // Store the next node temporarily
            ListNode* temp = curr->next;

            // Reverse the direction of the link for the current node
            curr->next = prev;

            // Shift the pointers forward
            prev = curr;
            curr = temp;
        }

        // After the loop, 'prev' will be pointing to the new head of the reversed list
        return prev;
    }
};