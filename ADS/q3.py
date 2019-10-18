#q3.py
#algorithms and data structures assignment 2018-19 question 3
#matthew johnson 21 november 2018

#####################################################

"""See adspractical4.py for further explanations of the usage of stacks
and queues."""

#####################################################

class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

########
#STACKS#
########

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data
    def out(self):
        s = self
        top = s.top()
        while(not s.isEmpty()):
            print(s.pop())

########
#QUEUES#
########

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def dequeue(self):
        output = self.front.data
        self.front = self.front.after
        if self.front == None:
            self.rear = None
        return output
    def enqueue(self, data):
        if self.rear == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.after = Node(data, self.rear)
            self.rear = self.rear.after
    
#####################################################
            

def testq3():
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4") 
    assert not good_expression("1*2+(3+4)")
    assert good_expression("(1+2)*3+4")
    assert good_expression("1+2*3+4")
    assert good_expression("1*2+3+4")
    assert not good_expression("1+(2*3)+4")
    assert not good_expression("1*2+(3+4)")
    assert good_expression("(1+2*3*((4+5)*6+7)+8)*9")
    print ("all tests passed")
    
#####################################################
def good_expression(string):
    #Initialize stack
    stack = Stack()
    """
    Initialize a second stack to store knowledge about bracket group
    hasMult stores whether there is a multiplication before a bracket set
    hasAdd stores whether there is an addition (lower precedence operator) in a bracket set
    """
    groupStack = Stack()
    #Iterate through. We need i to preload the next character so can't use a foreach style loop
    for i in range(0, len(string)):
        c = string[i]
        if c != ')':
            """
            If we find an opening bracket, reset our bracket set flag vars
            If the stack has something on it (i.e. this is not first item), check if it
            was a multiplication (higher precedence operator) and set flag to True if it was
            """
            if c == '(':
                groupStack.push({'hasMult':False, 'hasAdd':False})
                if not stack.isEmpty():
                    top = stack.top()
                    if top == '*':
                        groupStack.top()['hasMult'] = True
            #Push whatever we found onto the stack
            stack.push(c)
        #Else, we are reading a closing bracket.
        else:
            #View the top element, then pop it off.
            top = stack.top()
            stack.pop()
            """
            While we haven't reached an opening bracket (gone through a whole group),
            pop off elements.
            If the current top element is add, then there is an addition in the bracket
            group so set the flag to True
            """
            while top != '(':
                if top == '+':
                    groupStack.top()['hasAdd'] = True
                top = stack.top()
                stack.pop()
            """
            If there is another item (we are not at end of input)...
            """
            if i + 1 < len(string) - 1:
                """
                If there was no addition in the bracket group or no multiplication
                before or after the bracket group, then the group is considered invalid.
                """
                if not groupStack.top()['hasAdd'] == True or (groupStack.top()['hasAdd'] == True and not groupStack.top()['hasMult'] == True and string[i + 1] != '*'):
                    return False
            elif i == len(string) - 1 and not groupStack.top()['hasMult'] == True:
                """
                If there is a closing bracket at the end and there was no multiplication beforehand
                then the brackets are invalid.
                """
                return False
            groupStack.pop()
    return True

testq3()
