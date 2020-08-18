---
bookCollapseSection: true
weight: 2
title: "算法"
---

# 算法

* 冒泡排序

对于一个无序的序列，每次对比两个相邻数的大小，若第i个数大于第i+1个数，两个数进行位置互换。每组排序可以选出一个最大的数，然后继续从第一个数开始进行对比，直到完成排序
    
```go
// golang
func bubbleSort(nums []int) {
	for i := 0; i < len(nums)-1; i++ {
		for j := 0; j < len(nums)-1-i; j++ {
			if nums[j] > nums[j+1] {
				nums[j], nums[j+1] = nums[j+1], nums[j]
			}
		}
	}
	fmt.Println(nums)
}
```


* 选择排序

对于一个无序的序列，从第一个数开始，每次跟接下去的数对比，若第1个数小于第i个数，两个数位置互换，每次选出最小的数，然后开始对比第二个数，直到完成排序。

```go
// golang
func selectSort(nums []int) {
	for i := 0; i < len(nums)-1; i++ {
		min := i
		for j := i + 1; j < len(nums); j++ {
			if nums[j] < nums[min] {
				min = j
			}
		}

		if min != i {
			nums[i], nums[min] = nums[min], nums[i]
		}
	}
	fmt.Println(nums)
}

```

* 归并排序

对于一个无序的序列，将序列用递归的方式划分成左右两个序列，然后依次排序合并序列。

    #伪代码
    func sorted(int num[]){
        if(num.length<=1){
            return num[0]
        }
        leftnum = xxx
        rightnum = xxx
    
        sorted(leftnum[])
        sorted(rightnum[])
        merge(leftnum,rightnum)
    }


