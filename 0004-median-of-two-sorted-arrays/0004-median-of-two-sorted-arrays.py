class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # mergesort
        i, j = 0, 0
        index = 0
        res = []
        mid = (len(nums1)+len(nums2))//2

        while index<=mid and (i<len(nums1) or j<len(nums2)):
            if i<len(nums1) and j<len(nums2):
                if nums1[i]<=nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
                index += 1
            elif i<len(nums1):
                res.extend(nums1[i:])
                i += (len(nums1)-i)
                index = len(nums1)+len(nums2)
            else:
                #j<len(nums2)
                res.extend(nums2[j:])
                j += (len(nums2)-j)
                index = len(nums1)+len(nums2)
        
        
        if (len(nums1)+len(nums2)) % 2:
            return res[mid]
        else:
            return (res[mid] + res[mid-1])/2
