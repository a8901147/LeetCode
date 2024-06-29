/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    int counter = k;
    struct ListNode* prev_last = NULL;
    struct ListNode* first = NULL;
    struct ListNode* cur = head;

    struct ListNode* prev = NULL;
    struct ListNode* nxt = NULL;
    while(cur){
        // get first node
        first = cur;

        // loop k times
        while (counter && cur){
            cur = cur->next;
            counter -= 1;
        }

        if (counter){
            break;
        }
        else{
            //reverse list
            cur = first;
            for (int i = 0; i<k; i++){
                nxt = cur->next;
                cur->next=prev;

                prev = cur;
                cur = nxt;
            }
            
            if(!prev_last){
                head = prev;
            }

            // connect two list
            if (prev_last){
                prev_last->next = prev;
            }
            
            first->next = cur;
            prev_last = first;
            counter = k;
        }
    }
    return head;
}