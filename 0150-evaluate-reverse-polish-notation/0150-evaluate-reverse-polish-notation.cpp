class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;

        for (string c : tokens) {
            if ( c=="+" || c=="-" || c=="*" || c=="/") {
                int result = 0;
                int number2 = stack.top();
                stack.pop();
                int number1 = stack.top();
                stack.pop();
                if (c == "+") {
                    result = number1 + number2;
                }
                else if (c == "-") {
                    result = number1 - number2;
                }
                else if (c == "*") {
                    result = number1 * number2;
                }
                else if (c == "/") {
                    result = number1 / number2;
                }
                stack.push(result);
            }
            else {
                stack.push(stoi(c));
            }
        }
        return stack.top();
    }
};