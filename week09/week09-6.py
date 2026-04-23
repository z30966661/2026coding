# week09-6.py 學習計畫 Linked list 第2題
# LeetCode 328. Odd Even Linked List 偶數堆、奇數堆,串起來
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head:
            a.append( head.val )
            head = head.next # 這行圖中被截掉，但邏輯上必須要有

        N = len(a) # 這行圖中沒顯示，但第 15 行有用到 N
        now = ans = ListNode()

        # 先處理奇數索引位置 (1st, 3rd, 5th...)
        for i in range(0, N, 2):
            now.next = ListNode( a[i] )
            now = now.next

        # 再處理偶數索引位置 (2nd, 4th, 6th...)
        for i in range(1, N, 2):
            now.next = ListNode( a[i] )
            now = now.next

        return ans.next
