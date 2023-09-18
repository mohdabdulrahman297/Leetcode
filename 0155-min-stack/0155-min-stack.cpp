#include <iostream>
#include <stack>

class MinStack {
public:
    std::stack<int> stack; // Regular stack
    std::stack<int> minStack; // Stack to keep track of the minimum value

    void push(int val) {
        // Append values into the stack
        stack.push(val);

        // Check minimum values from the top of the minStack and the input value
        if (!minStack.empty()) {
            val = std::min(val, minStack.top());
        }

        minStack.push(val);
    }

    void pop() {
        if (!stack.empty()) {
            stack.pop();
            minStack.pop();
        }
    }

    int top() {
        if (!stack.empty()) {
            return stack.top();
        }
        return -1; // Handle the case when the stack is empty
    }

    int getMin() {
        if (!minStack.empty()) {
            return minStack.top();
        }
        return -1; // Handle the case when there is no minimum value
    }
};

