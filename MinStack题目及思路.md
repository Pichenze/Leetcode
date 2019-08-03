# Leetcode
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。


	push(x) -- 将元素 x 推入栈中。
	pop() -- 删除栈顶的元素。
	top() -- 获取栈顶元素。
	getMin() -- 检索栈中的最小元素。


示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


思路：
最粗略版本：
在定义Stack的同时，在拥有存储堆栈的列表content以及栈顶栈底指针topp,base的同时（其实base没什么用）
还添加成员min用于记录当前栈的最小值，每次使用push,pop都需要判断当前最小值是否变化，因此，如果栈顶是最小值的话，需要重新遍历content列表进行查找，
是一个比较简单粗暴的思想。
