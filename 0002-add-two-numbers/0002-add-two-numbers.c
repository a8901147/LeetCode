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

    while (l1 || l2 || carry){
        sum = 0;
        if (l1){
            sum += l1->val;
            l1 = l1->next;
        }

        if(l2){
            sum += l2->val;
            l2 = l2->next;
        }

        sum += carry;

        carry = sum/10;
        sum = sum%10;

        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node -> next = NULL;
        new_node -> val = sum;

        cur->next = new_node;
        cur = cur->next;
    }

    return head->next;
}