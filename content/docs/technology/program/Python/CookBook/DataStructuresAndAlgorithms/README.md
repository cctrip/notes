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

10. 删除列表的重复项

	问题，排除列表中的重复项，并保留顺序。

	实现，[详细代码](10.py)

		>>> seen = set()
		>>> for item in [1,3,5,9,1]:
		...     if item not in seen:
		...         seen.add(item)
		>>> list(seen)
		[1, 3, 5, 9]

11. 命名一个分片

	问题，清除混乱的内容

	实现，[详细代码](11.py)

		>>> record = '....................100          .......513.25     ..........'
		>>> SHARES = slice(20,32)
		>>> PRICE = slice(40,48)
		>>> cost = int(record[SHARES]) * float(record[PRICE])
		>>> print(cost)
		51325.0

12. 查找队列中最常出现的item

	问题，有一个队列，想找出出现最频繁的item

	实现，[详细代码](12.py)

		>>> from collections import Counter
		>>> words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes','look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',]
		>>> word_counts = Counter(words)
		>>> top_two = word_counts.most_common(2)
		>>> print(top_two)
		[('look', 4), ('into', 4)]

13. 根据公共的key排序字典列表

	问题，你有一个字典的列表，你想根据一个或多个字典值排序条目。

	实现，[详细代码](13.py)

		>>> rows = [ {'fname':'Brain','uid':1003},
		... {'fname':'Jhon','uid':1002},
		... {'fname':'Alin','uid':1005}]
		>>> from operator import itemgetter
		>>> rows_by_uid = sorted(rows,key=itemgetter('uid'))
		>>> print(rows_by_uid)
		[{'fname': 'Jhon', 'uid': 1002}, {'fname': 'Brain', 'uid': 1003}, {'fname': 'Alin', 'uid': 1005}]

14. 排序不支持比较的对象

	问题，你想对同一类对象进行排序，但它本身并不支持比较

	实现，[详细代码](14.py)

15. 基于特定字段的值进行分组

	问题，有一系列字典或实例，希望根据特定字段的值来迭代数据，例如日期。

	实现，[详细代码](15.py)

16. 过滤队列中的元素

	问题，你有一个队列需要通过某些标准提取或者减少值

	实现，[详细代码](16.py)

		>>> mylist = [1, 4, 3, -2, 5, 0]
		>>> [n for n in mylist if n > 0]
		[1, 4, 3, 5]

17. 提取字典的子集

	问题，制作一个字典是另一个字典的一个子集

	实现，[详细代码](17.py)

18. 名称映射到序列中的元素

	问题，通过按名称访问元素，减少对结构中的位置的依赖

	实现，[详细代码](18.py)

		>>> from collections import namedtuple
		>>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
		>>> sub = Subscriber('test@examole.com', '2017-07-31')
		>>> sub
		Subscriber(addr='test@examole.com', joined='2017-07-31')
		>>> sub.addr
		'test@examole.com'
		>>> sub.joined
		'2017-07-31'

19. 同时转换和减少数据

	问题，您需要执行缩减功能(例如sum(),min(),max()),但首先需要转换或过滤数据.

	实现，[详细代码](19.py)
		>>> nums = [1,2,3,4,5]
		>>> s = sum(x*x for x in nums)
		>>> print(s)
		55

20. 将多个映射组合成单个映射

	问题，您有多个字典或映射，您要逻辑组合成一个映射来执行某些操作，例如查找值或检查键的存在

	实现，[详细代码](20.py)

		>>> a = {'x': 1, 'z': 3 }
		>>> b = {'y': 2, 'z': 4 }
		>>> from collections import ChainMap
		>>> c = ChainMap(a,b)
		>>> c
		ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})