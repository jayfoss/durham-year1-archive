def MergeSort(m):
    """
    If the length is less than or equal to 1, just return
    since we don't even need to run SelectionSort
    """
    if len(m) <= 1:
        return m
    #Calculate the midpoint and cast to int so there is no decimal
    middle = int(len(m) / 2)
    #Init some empty arrays. ls/rs are sorted
    l = []
    r = []
    ls = []
    rs = []
    #The left half must go from 0 to the midpoint (exclusive)
    l = m[0:middle]
    #The right half must go from the midpoint and capture all elements to the end
    r = m[middle:]
    """
    If the length is less than or equal to 4, use SelectionSort, as specified in the Q6a brief
    If not, use MergeSort
    """
    if len(l) <= 4:
        ls = SelectionSort(l)
    else:
        ls = MergeSort(l)
    if len(r) <= 4:
        rs = SelectionSort(r)
    else:
        rs = MergeSort(r)
    #Merge the parts together
    return Merge(ls, rs)

def Merge(l, r):
    result = []
    #While one of the halves is not empty...
    while(len(l) > 0 or len(r) > 0):
        #If they're both not empty...
        if len(l) > 0 and len(r) > 0:
            #Check if first element in left is greater or equal than right
            if l[0] >= r[0]:
                #If it is, append it to result
                result.append(l[0])
                #Remove the element that has been added to result
                l = l[1:]
            else:
                #If not, first element in right must be greater so use it instead
                result.append(r[0])
                r = r[1:]
        elif len(l) > 0:
            """
            If only left has something
            Add whatever remaining items are on left to result and clear left
            """
            result += l
            l = []
        else:
            """
            If only right has something
            Add whatever remaining items are on right to result and clear right
            """
            result += r
            r = []
    return result

def SelectionSort(listPart):
    #Location of max has not yet been found
    maxLoc = -1
    #Iterate through list
    for i in range(len(listPart)):
        #Set maxLoc to be the current element
        maxLoc = i
        #Iterate through remaining elements of list in front of i
        for j in range(i + 1, len(listPart)):
            #If the j element is greater than the one at current maxLoc, set maxLoc to be j
            if listPart[j] > listPart[maxLoc]:
                maxLoc = j
        #Switch the element at i with the one at maxLoc.
        listPart[i], listPart[maxLoc] = listPart[maxLoc], listPart[i]
    return listPart
