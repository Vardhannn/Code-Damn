#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct Stack {
    int top;
    unsigned capacity;
    char* array;
};

struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (char*)malloc(stack->capacity * sizeof(char));
    return stack;
}

int isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

int precedence(char ch) {
    switch(ch) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

void push(struct Stack* stack, char item) {
    stack->array[++stack->top] = item;
}

char pop(struct Stack* stack) {
    if (stack->top == -1)
        return '\0';
    return stack->array[stack->top--];
}

char peek(struct Stack* stack) {
    return stack->array[stack->top];
}

void infixToPostfix(char* infix, char* postfix) {
    struct Stack* stack = createStack(strlen(infix));
    int i, k;
    char ch;

    for (i = 0, k = -1; infix[i]; ++i) {
        if (isdigit(infix[i]) || isalpha(infix[i])) {
            postfix[++k] = infix[i];
        }
        else if (infix[i] == '(') {
            push(stack, infix[i]);
        }
        else if (infix[i] == ')') {
            while (stack->top != -1 && peek(stack) != '(') {
                postfix[++k] = pop(stack);
            }
            if (stack->top != -1 && peek(stack) != '(') {
                printf("Invalid Expression\n");
                return;
            } else {
                pop(stack);
            }
        } else {
            while (stack->top != -1 && precedence(infix[i]) <= precedence(peek(stack))) {
                postfix[++k] = pop(stack);
            }
            push(stack, infix[i]);
        }
    }

    while (stack->top != -1) {
        postfix[++k] = pop(stack);
    }
    postfix[++k] = '\0';
}

int main() {
    char infix[100];
    printf("Enter an infix expression: ");
    scanf("%s", infix);

    char postfix[100];
    infixToPostfix(infix, postfix);
    printf("Postfix expression: %s\n", postfix);

    return 0;
}
