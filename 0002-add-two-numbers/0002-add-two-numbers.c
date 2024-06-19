/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    head->next = NULL;
    struct ListNode* cur = head;
    int carry = 0;
    int sum;

    while (l1 || l2){
        if (l1 && l2){
            sum = l1->val+l2->val+carry;
            l1 = l1->next;
            l2 = l2->next;
        }
        else if(l1){
            sum = l1->val+carry;
            l1 = l1->next;
        }
        else if (l2){
            sum = l2->val+carry;
            l2 = l2->next;
        }
        carry = sum/10;
        sum = sum%10;

        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node -> next = NULL;
        new_node -> val = sum;

        cur->next = new_node;
        cur = cur->next;
    }
    if (carry){
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node -> next = NULL;
        new_node -> val = 1;

        cur->next = new_node;
        cur = cur->next;
    }
    return head->next;
    
}