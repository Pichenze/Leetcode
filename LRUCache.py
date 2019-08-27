from collections import OrderedDict  #有序字典
# 时间复杂度：对于 put  和 get 操作复杂度是 O(1)O(1)O(1)，因为有序字典OrderedDict中的所有操作：get/in/set/move_to_end/popitem（get/containsKey/put/remove）都可以在常数时间内完成。
# 空间复杂度：O(capacity)O(capacity)O(capacity)，因为空间只用于有序字典存储最多 capacity + 1 个元素。

class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    # get或put时都要更新最近使用到的key,使用move_to_end可以直接把它放在最后面
    # 而最近最少使用的则会在有序字典的前面，使用popitem就可以将它去掉
    def get(self, key: int) -> int:
        if key not in self:
        	return -1
        self.move_to_end(key)  # 将最新get得到的key放在有序字典的最后，保证最近最少使用的在有序字典前面
        return self[key]


    def put(self, key: int, value: int) -> None:
        if key in self:
        	self.move_to_end(key)  # 将最近put的key放在有序字典的最后，保证最近最少使用的在有序字典前面
        self[key] = value
        if len(self) > self.capacity:
        	self.popitem(last = False)

    def printd(self):
    	for key in self:
    		print(key,':',self[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
	cache = LRUCache(2)
	cache.put(1,1)
	cache.printd()
	cache.put(2,2)
	cache.printd()
	cache.get(1)       # 返回  1
	cache.put(3,3)
	cache.printd()    # 该操作会使得密钥 2 作废
	cache.get(2)     # 返回 -1 (未找到)
	cache.put(4,4)
	cache.printd()    # 该操作会使得密钥 1 作废
	cache.get(1)       # 返回 -1 (未找到)
	cache.get(3)       # 返回  3
	cache.get(4)
	cache.printd()
