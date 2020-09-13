---
bookCollapseSection: false
weight: 1
title: "数组"
---

# 数组

## 什么是数组？

>An Array is a collection of items. The items could be integers, strings, DVDs, games, books—anything really. The items are stored in neighboring (contiguous) memory locations. Because they're stored together, checking through the entire collection of items is straightforward.

***

## 数组的CRUD

### 创建和访问数组

```go
//数组，长度不可变
//切片，长度可变
func arraySlice() {
	//创建数组(声明长度)
	var array1 = [5]int{1, 2, 3}

	//创建数组(不声明长度)
	var array2 = [...]int{6, 7, 8}

	//创建切片
	var array3 = []int{9, 10, 11, 12}

	//创建数组(声明长度)，并仅初始化其中的部分元素
	var array4 = [5]string{3: "Chris", 4: "Ron"}

	//创建数组(不声明长度)，并仅初始化其中的部分元素，数组的长度将根据初始化的元素确定
	var array5 = [...]string{3: "Tom", 2: "Alice"}

	//创建切片，并仅初始化其中的部分元素，数组切片的len将根据初始化的元素确定
	var array6 = []string{4: "Smith", 2: "Alice"}
  
  //创建切片
  array7 := make([]int, length, capacity)
  
  //访问数组，通过index访问
  fmt.Println(array7[0])
}
```

***

### 数组插入元素

```go
func insert() {
  var array []int
	//插入元素到结尾
  array = append(array,6)

	//插入元素到开头,需要先把数组后移，再插入元素
  for i:=len(array)-1;i>=0;i-- {
    array[i+1] = array[i]
  }
  array[0] = 10

	//插入元素到指定位置，先把指定位置及后面的数据后移，再插入元素
  set := 2
  for i := len(array)-1;i>=set;i--{
    array[i+1] = array[i]
  }
  array[set] = 10
}
```

***

### 数组删除元素

```go
func delete() {
  array := []int{1,2,3}
  //从尾部删除元素
  array = array[:len(array)-1]
  
  //从开头删除元素，把数据前移，删除最后一位
  for i := 1; i < len(array); i++) {
    array[i-1] = array[i]
	}
  array = array[:len(array)-1]
  
  //从指定位置删除元素，把指定位置后面的数据前移，再删除最后一位
  for i := 2; i < len(array); i++) {
    array[i-1] = array[i]
	}
  array = array[:len(array)-1]
}
```

***

### 搜索某个元素

```go
func search(num int) bool {
  //线性搜索
  array := []int{1,2,3}
  for i:=0; i<len(array); i++{
    if array[i] == num {
       return true
    }
  }
  return false
}
```

***

### 就地操作数组

节省时间和空间

***

### 删除重复元素

```go
func removeDuplicates(nums []int) {
	if len(nums) == 0 {
		return
	}
	writePointer := 1
	for readPointer := 1; readPointer < len(nums); readPointer++ {
		if nums[readPointer] != nums[readPointer-1] {
			nums[writePointer] = nums[readPointer]
			writePointer++
		}
	}
	fmt.Println(nums[:writePointer])
}
```

