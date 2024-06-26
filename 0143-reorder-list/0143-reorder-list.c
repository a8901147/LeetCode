/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

// Function to reverse the linked list from the starting node
struct ListNode* reverse(struct ListNode* start) {
    struct ListNode* prev = NULL;
    struct ListNode* current = start;
    struct ListNode* next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

void reorderList(struct ListNode* head) {
    struct ListNode* slow = head;
    struct ListNode* fast = head;
    while (fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }

     // Reverse the second half of the list
    struct ListNode *second = reverse(slow->next);
    slow->next = NULL; // Split the list into two parts
    
    // Merge the two halves
    struct ListNode *first = head;
    while (first && second) {
        struct ListNode *temp1 = first->next;
        struct ListNode *temp2 = second->next;

        first->next = second;
        second->next = temp1;

        first = temp1;
        second = temp2;
    }
}