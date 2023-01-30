# ========== .data is the 0th item in the 2D list
# ========== .pointer is the 1st item in the 2D list
# ========== mylist[0][0] = startPointer
# ========== mylist[0][1] = freeListPtr

NULLPOINTER = 0


def initialise_list(mylist):
    startPointer = NULLPOINTER
    freeListPtr = 1
    mylist.append([])

    # assign freeListPtr & startPointer to the list's 0th 2D list
    mylist[0].append(startPointer)
    mylist[0].append(freeListPtr)

    # initialise every item
    for i in range(1, 6):
        mylist.append([])
        mylist[i].append("")
        mylist[i].append(i + 1)
    mylist.append(["", NULLPOINTER])


def assign_fs_pointer(mylist):
    return mylist[0][0], mylist[0][1]


def assign_fs_back(mylist, startPointer, freeListPtr):
    mylist[0][0] = startPointer
    mylist[0][1] = freeListPtr


def insert_node(newItem, mylist):
    startPointer, freeListPtr = assign_fs_pointer(mylist)
    #       0       1
    if freeListPtr != NULLPOINTER:
        newNodePtr = freeListPtr  # 1
        mylist[newNodePtr][0] = newItem  # [1][0] = 2
        freeListPtr = mylist[freeListPtr][1]  # 2

        thisNodePtr = startPointer  # 1

        # previousNodePtr = thisNodePtr  # 1
        #               False                                    2 !< 2
        while thisNodePtr != NULLPOINTER and mylist[thisNodePtr][0] < newItem:
            previousNodePtr = thisNodePtr  # 1
            thisNodePtr = mylist[thisNodePtr][1]  # 2
        #               1 = 1
        if previousNodePtr == startPointer:
            mylist[newNodePtr][1] = startPointer  # [2][1] = 1
            startPointer = newNodePtr  # 2
        else:
            mylist[newNodePtr][1] = mylist[previousNodePtr][1]
            mylist[previousNodePtr][1] = newNodePtr

    # not sure about this line
    assign_fs_back(mylist, startPointer, freeListPtr)


def find_node(dataItem, mylist):
    startPointer, freeListPtr = assign_fs_pointer(mylist)

    currentNodePtr = startPointer
    while currentNodePtr != NULLPOINTER and mylist[currentNodePtr][0] != dataItem:
        currentNodePtr = mylist[currentNodePtr][1]
    return currentNodePtr


def delete_node(dataItem, mylist):
    startPointer, freeListPtr = assign_fs_pointer(mylist)

    thisNodePtr = startPointer
    while thisNodePtr != NULLPOINTER and mylist[thisNodePtr][0] < dataItem:
        previousNodePtr = thisNodePtr
        thisNodePtr = mylist[thisNodePtr][1]
    if thisNodePtr != NULLPOINTER:
        if thisNodePtr == startPointer:
            startPointer = mylist[startPointer][1]
        else:
            mylist[previousNodePtr] = mylist[thisNodePtr][1]
        mylist[thisNodePtr][1] = freeListPtr
        freeListPtr = thisNodePtr
    assign_fs_pointer(mylist, startPointer, freeListPtr)


def output_all_nodes(mylist):
    startPointer, freeListPtr = assign_fs_pointer(mylist)
    currentNodePtr = startPointer
    while currentNodePtr != NULLPOINTER:
        print(mylist[currentNodePtr][0])
        currentNodePtr = mylist[currentNodePtr][1]


mylist = []
initialise_list(mylist)
print(mylist)

insert_node(2, mylist)
print(mylist)
