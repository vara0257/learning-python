class MyList:
    def __init__(self, list):
        self.list = list
        self.duplicateList = []
        self.uniqueList = []

    def display(self , list):
        """
            Display a list
        """
        print(list)

    def duplicate(self):
        for i in self.list:
            if self.list.count(i)>1:
                if self.duplicateList.count(i)<1:
                    self.duplicateList.append(i)
    
    def unique(self):
        for x in self.list:
            if x not in self.uniqueList:
                self.uniqueList.append(x)

    def linear(self, n):

        if n in self.list:
           return True
        return False
    
    def binary(self, n):
        bl=sorted(self.list)
        first=0
        last=len(bl)-1

        while first <= last:
            mid = (first+last)//2
            if n == bl[mid]:
                return True
            if n < bl[mid]:
                last = mid-1
            else:
                first = mid+1
        return False
        

list1 = MyList(list=[1, 1, 3, 2, 2, 4, 1, 5])
list1.display(list1.list)
list1.duplicate()
list1.display(list1.duplicateList)
list1.unique()
list1.display(list1.uniqueList)
print (list1.linear(10))
print (list1.binary(5))