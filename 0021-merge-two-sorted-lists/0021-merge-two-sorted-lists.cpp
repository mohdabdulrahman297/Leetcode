/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 
 
 // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int val = 0, ListNode* next = nullptr) : val(val), next(next) {}
};


 * RECURSIVE SOLUTION
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
       if(!list1){
           return list2;
       }
       if(!list2){
           return list1;
       }
        
       ListNode*lil = (list1->val < list2->val) ? list1 : list2;
       ListNode*big = (list1->val < list2->val) ? list2 : list1;
       lil->next = mergeTwoLists(lil->next, big);
        
       return lil;
    }
};