'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.

Note: A number is said to be evenly divisible if it is divisble by all the numbers in the given range without any reaminder.
Consider the range to be from 1 to 10 (both inclusive)
Assume that there will always be few elements in the input queue, which are evenly divisible by the  numbers in the mentioned
range.

Example:
Input Queue: 13983,10080,7113,2520,2500(front -rear)
Output Queue: 10080,2520(front-rear)'''


class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements=[None]*self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_Empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_Empty()):
            print("Queue is Empty")
        else:
            data = self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for i in range(self.__front,self.__rear+1):
            print(self.__elements[i])

    def get_max_size(self):
        return self.__max_size

    def even_div(self):
        q2 = Queue(self.__max_size)
        for i in range(self.__front,self.__rear+1):
            chk=0
            for j in range(1,11):
                if self.__elements[i]%j!=0:
                    chk=1
                    break
                   
            if(chk==0):        
                q2.enqueue(self.__elements[i])
        q2.display()
                                                
q=Queue(5)
q.enqueue(13983)
q.enqueue(10080)
q.enqueue(7113)
q.enqueue(2520)
q.enqueue(2500)
q.even_div()