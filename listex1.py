from collections import deque

l1 = ["sra","van","kum","ar","red","dy"]

l1_sub = ["rla","pati"]

print "kum present at ", l1.index("kum")

print "count of sra:",l1.count("sra");

l1.append("ga")

lt=("sra","van","kum","ar","red","dy");

#lt.append("ga");

print "after appending : list :",l1;

l1.extend(l1_sub)

print "after extending list:",l1;

l1.insert(0,"Mr.");

print "after inserting at fisrst postion : ",l1

l1.remove("Mr.");

print "after removing particular element:",l1;

l1.pop(3);

print "after pop :",l1


del l1[2];

print "deleting element at partcular position :", l1;

print "range ",l1[2:], "before colon",l1[:2];


queue = deque(["Eric", "John", "Michael"])
queue.popleft();
print "after pop left:",queue;

