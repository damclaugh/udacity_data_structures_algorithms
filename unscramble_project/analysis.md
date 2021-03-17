

Task 0 has a run-time effficiency of O(1) because the program just 
gets the first and last times of the lists. The time to run doesn't 
depend on the length of the list.

Task 1 has a run-time efficiency of O(n). Unlike Task 0, it loops
through the full lists of numbers. The longer the lists, the longer 
the time to run. The time increases at a linear rate with the size 
of the lists. Therefore, the efficiency is O(n). O(n) means for input 
of size n (in this case the size of the list), the number of operations 
needed is n.

Task 2 has a run-time efficiency of O(n) for the same reason as Task 1.

Tasks 3 has a run-time efficiency of O(n log n). Like Tasks 1 and 2, 
it loop through the lists, and the longer the lists, the number
of operations increases linearly. But after the loop, it has a sort 
function, which has time complexity of O(n log n). O(n log n) has a greater
run-time than O(n). 

Task 4 has a run-time efficiency of O(n log n) for the same reason as Task 3.