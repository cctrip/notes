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

	实现，[详细代码](4.py)

		>>> import heapq
		>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
		>>> heapq.nlargest(3,nums)
		[42, 37, 23]
		>>> heapq.nsmallest(3,nums)
		[-4, 1, 2]
