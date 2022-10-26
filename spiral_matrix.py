class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        down=len(matrix)
        left=0
        right=len(matrix[0])
        ans=[]
        while(top< down and left< right):
            for i in range (left,right):
                ans.append(matrix[top][i])
            top+=1
            for i in range (top,down):
                ans.append(matrix[i][right-1])
            right-=1
            if (top<down):
                for i in range (right-1,left-1,-1):
                    ans.append(matrix[down-1][i])
                down-=1
            if (left<right):
                for i in range (down-1,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
