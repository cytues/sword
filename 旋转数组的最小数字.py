# -*- coding:utf-8 -*-
'''
在算法上，考虑数字没有重复的情况的话，使用二分法，有两个指针，第一个指针指向front，第二个指针指向rear，
midIndex是中间数字，只要是旋转数组，那么首位一定大于中间位，所以如果首位大于中间位的话，那么就把指针从首位移到中间
位，前面数字向后移动，不断迭代，当首位和最后位只差1时，最后维就是最小值。此时最坏时间复杂度是O(logn),但是要考虑数字
重复的话，情况只可能是首位和末尾和中间重这种[1,0,1,1]只能取其中最小值，逐一排列，对于首位和中间位重的，比如[1,1,0],
把首位移动到后面去，可以处理，或者中间位和末尾重，比如[1,0,0]，也是能处理，其他情况不存在，因为前提要求是旋转数组
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        # 创建前后指针
        front, rear = 0, len(rotateArray) - 1
        # 中值数字
        midIndex = 0
        # 确保旋转
        while rotateArray[front] >= rotateArray[rear]:
            # 当首尾仅差距1时，最后位为最小值
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            # 无法确定中间元素是属于前面还是后面的递增子数组
            # 只能顺序查找
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.minOrder(rotateArray, front, rear)
            # 二分查找，又不同于二分查找，旋转之后的数组实际上可以划分成两个有序的子数组：
            # 前面子数组的大小都大于后面子数组中的元素
            # 中间元素大于第一个元素，则中间元素位于前面的递增子数组，
            # 此时最小元素位于中间元素的后面。我们可以让第一个指针front指向中间元素。
            if rotateArray[front] <= rotateArray[midIndex]:
                front = midIndex
            # 中间元素小于第一个元素，则中间元素位于后面的递增子数组，
            # 此时最小元素位于中间元素的前面。我们可以让第二个指针rear指向中间元素。
            elif rotateArray[rear] >= rotateArray[midIndex]:
                rear = midIndex

        return rotateArray[midIndex]

    # 顺序查找
    def minOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end + 1]:
            if i < result:
                result = i
        return result