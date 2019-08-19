# leecode 乘最多水的容器  https://leetcode-cn.com/problems/container-with-most-water/submissions/
# 双指针法： 时间复杂度O(n) ,空间复杂度O(1)
# 算法  https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode/
#这种方法背后的思路在于，两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。
#我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。 
#此外，我们会使用变量 max(area,maxarea) 来持续存储到目前为止所获得的最大面积。 
# 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxarea，并将指向较短线段的指针向较长线段那端移动一步。


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left,right = 0,len(height)-1 #双指针，一个在开头，一个在末尾
        while left!= right:
            # 判断 两个指针哪个指针所指向的高度比较低，把高度低的指针往里靠近一格，
            if height[left] < height[right]:  
                maxArea = max(maxArea,(right-left)*height[left])
                left += 1  
            else:
                maxArea = max(maxArea,(right-left)*height[right])
                right -= 1
        return maxArea
