### 数据结构和算法

1. 解压序列赋值给多个变量

	问题，现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变量？

	实现：[详细代码](1.py)

		>>> data = ['John',170,60,(1999,9,9)]
		>>> name, height, weight, birthday = data
		### 另一种方式
		>>> name, height, weight, (year, mon, day) = data


2. 解压可迭代对象赋值给多个变量

	问题，如果一个可迭代对象的元素个数超过变量个数时，会抛出一个ValueError。那么怎样才能从这个可迭代对象中解压出N个元素出来？

	实现：[详细代码](2.py)

		>>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
		>>> name, email, *phone_numbers = record

3. 保留最后N个元素

	问题，在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

	实现：[详细代码](3.py)

		>>> from collections import deque
		>>> q = deque(maxlen = 3)
		>>> q.append(1)
		>>> q.append(2)
		>>> q.append(3)
		>>> q
		deque([1, 2, 3], maxlen=3)
		>>> q.append(4)
		>>> q
		deque([2, 3, 4], maxlen=3)

4. 查找最大或最小的N个元素

	问题，怎样从一个集合中获得最大或者最小的N个元素列表？

	实现：[详细代码](4.py)

		>>> import heapq
		>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
		>>> heapq.nlargest(3,nums)
		[42, 37, 23]
		>>> heapq.nsmallest(3,nums)
		[-4, 1, 2]

5. 实现优先级队列

	问题，给定一个具有优先级的队列，每次pop操作取出优先级最高的Item

	实现：[详细代码](5.py)

		>>> from heapq import heappush, heappop
		>>> heap = []
		>>> data = [(2,'A'),(7,'B'),(5,'C')]
		>>> for item in data:
		...     heappush(heap, item)
		... 
		>>> print(heappop(heap)[-1])
		A
		>>> print(heappop(heap)[-1])
		C
		>>> print(heappop(heap)[-1])
		B

6. 字典中将键映射到多个值

	问题，字典是每个键映射到单个值的映射。如果要将键映射到多个值，则需要将多个值存储在另一个容器中，例如列表或集合。

	实现：[详细代码](6.py)

		>>> d = {'a':[1,2,3],'b':[4,5]}
		>>> d = {'a':{1,2,3},'b':{4.5}}
		#另一种实现
		>>> from collections import defaultdict
		>>> d = defaultdict(list)
		>>> d['a'].append(1)
		>>> d['a'].append(2)
		>>> d['b'].append(4)

7. 有序字典
	
	问题，想使用字典，并且想在迭代的时候控制输出顺序。

	实现,：[详细代码](7.py)

		>>> from collections import OrderedDict
		>>> d = OrderedDict()

8. 用字典计算

	问题，想用字典内的数据做各种计算(最大值，最小值，排序等)

	实现：[详细代码](8.py)

		>>> prices = {'APPLE':23.33,'ORANGE':33.55,'BANANA':11.23}
		>>> print(min(zip(prices.values(),prices.keys())))
		(11.23, 'BANANA')
		>>> print(max(zip(prices.values(),prices.keys())))
		(33.55, 'ORANGE')
		>>> print(sorted(zip(prices.values(),prices.keys())))
		[(11.23, 'BANANA'), (23.33, 'APPLE'), (33.55, 'ORANGE')] 

9. 查找两个字典的共性

	问题，比对两个字典，返回两个字典的共性。

	实现，[详细代码](9.py)

		>>> a = {'x':1,'y':2,'z':3}
		>>> b = {'w':10,'x':11,'y':2}
		>>> a.keys() & b.keys()
		{'x', 'y'}
		>>> a.keys() - b.keys()
		{'z'}
		>>> a.items() & b.items()
		{('y', 2)}