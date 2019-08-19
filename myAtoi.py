class Solution:
	'''
	num保存要返回的数值, sig保存数字正负符号
	先用j指针找到数字的开头，数字的开头一般只可能是'+','-','0-9'；
							如果是' '那么可以对下一个字符检测，如果是其他字符，表示最开头不是数字，直接返回0

	在用j指针进行检测之后，那么从j+1开始如果不是'0-9'的数字的话，就可以直接退出循环了（不再计算num了，因为后面的计算都不重要了）
	                    考虑一些情况 +-2
	                                -x
	                                3235b
	                                3
	                                4534
	                                -25123x           
	'''
    def myAtoi(self, str: str) -> int:
        num = 0
        sig = 1
        j = 0
        while j < len(str):
            if str[j]==' ':
                j += 1
                continue
            elif str[j]=='-':
                sig = -1
                break
            elif str[j]=='+':
                sig = 1
                break
            elif str[j]>='0' and str[j]<='9':
                num *= 10
                num += int(str[j])-int('0')
                break
            else:
                return 0
            j += 1
        
        if j < len(str):
            for i in range(j+1,len(str)):
                if str[i] > '9' or str[i]<'0':
                    break
                else:
                    num *= 10
                    num += int(str[i])-int('0')
        INT_MAX,INT_MIN = 0xffffffff//2,-0xffffffff//2
        if sig*num > INT_MAX:
            return INT_MAX
        elif sig*num < INT_MIN:
            return INT_MIN
        return sig*num
