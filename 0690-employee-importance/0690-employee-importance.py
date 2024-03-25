"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_map = {}
        for employee in employees:
            employees_map[employee.id] = employee 
        
        def dfs(employee_id):
            res = employees_map[employee_id].importance
            for sub_id in employees_map[employee_id].subordinates:
                res += dfs(sub_id)
            return res


        return dfs(id)
        