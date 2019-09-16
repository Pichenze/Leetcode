class Solution:
    def addTwoNumbers(self, l1, l2):
            head = node = ListNode(0)
            c = 0
            while l1 and l2:
                node.next = ListNode((l1.val+l2.val+c)%10)
                c = (l1.val+l2.val+c)//10
                l1 = l1.next
                l2 = l2.next
                node = node.next
            while l1:
                node.next = ListNode((l1.val+c)%10)
                c = (l1.val+c)//10
                l1 = l1.next
                node = node.next
                if c == 0:
                    node.next = l1
                    break
            while l2:
                node.next = ListNode((l2.val+c)%10)
                c = (l2.val+c)//10
                l2 = l2.next
                node = node.next
                if c == 0:
                    node.next = l2
                    break
            if c != 0:
                node.next = ListNode(c)
                node = node.next
            return head.next
