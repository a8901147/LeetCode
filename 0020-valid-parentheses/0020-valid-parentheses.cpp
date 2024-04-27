class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (char c : s) {
            if ( c=='(' || c=='{' || c=='[') {
                stack.push(c);
                continue;
            }

            if (stack.empty()) {
                return false;
            }

            char lastest = stack.top();
            if( ( c==')' && lastest != '(') ||( c==']' && lastest != '[')||( c=='}' && lastest != '{')){
                return false;
            }
            stack.pop();
        }
        return stack.empty();
    }
};