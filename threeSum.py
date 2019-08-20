class Solution:
    '''
    首先对数组进行排序
    然后使用三个指针：low,mid,high 来分别定位三个数字
    low指针在最前头，从第一个数慢慢往前增加（不会回退）
    而mid和high使用双指针策略进行变更，mid初始化为low+1,high初始化为最后一个数字的索引也就是len(nums)-1
    然后根据 sortnums[low]+sortnums[mid]+sortnums[high] 与 0的关系对mid进行后靠操作或是对high进行前靠操作（low在此时保持不变），
    直到mid>=high说明这两个指针已经相遇，这个时候说明已经不再有多的包含sortnums[low]的三元组满足相加为3的情况了，这个时候对low进行靠后操作，然后重复上面的步骤，直到low达到len(nums)-2
    
    整个过程中low作为相对固定的指针（当sortnum[low]为x时，表示此刻正在寻找包含x的三元组满足三数之和为0），使用mid和high进行双指针检测
    '''
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        ans = []
        sortnums = sorted(nums)
        low,high = 0,len(sortnums)-1
        mid = low + 1
        print(sortnums)
        while low < len(sortnums)-2 and sortnums[low] <= 0:
            mid = low+1
            high = len(sortnums)-1
            #print(low,mid,high)
            while mid < high:
                if sortnums[low]+sortnums[mid]+sortnums[high] < 0:
                    mid += 1
                elif sortnums[low]+sortnums[mid]+sortnums[high] > 0:
                    high -= 1
                elif sortnums[low]+sortnums[mid]+sortnums[high] == 0:
                    ans.append([sortnums[low],sortnums[mid],sortnums[high]])
                    while mid < high-1 and sortnums[high] == sortnums[high-1]: #防止mid往后靠后，和前面的值还是一样，出现冗余的情况,所以要多次靠后，直到mid对应的值和之前的不一样
                        high -= 1
                    while mid+1 < high and sortnums[mid] == sortnums[mid+1]: # 和mid一样的道理，防止结果冗余
                        mid += 1

                    # *注意：记得循环结束的条件是mid和mid+1对应的值不同，但是此时mid对应的值还是那个相同的值，所以要多进行一次mid+=1
                    high -= 1
                    mid += 1
                    print(mid,high)
            while low+1 < len(sortnums)-2 and sortnums[low]==sortnums[low+1]: #和mid一样的道理，防止low往后靠后，和前面的值还是一样，出现冗余的情况
                low += 1
            low += 1
        return ans    

if __name__ == '__main__':
    a = [-1,0,1,2,-1,-4]
    solu = Solution()
    print(solu.threeSum(a))
