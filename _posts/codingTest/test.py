from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        result = 0
        
        while operations:
            target = operations.pop(0)

            try:
                operation = int(target)
                record.append(operation)
            except Exception as e:
                if target == 'C':
                    record.pop()
                elif target == 'D':
                    if abs(record[len(record) - 1]) < 0:
                        record.append((record[len(record) - 1] * 2) * -1)
                    else:
                        record.append(record[len(record) - 1] * 2)
                elif target == '+':
                    record.append(record[len(record) -2] + record[len(record) - 1])
            
            print(record)
            
        return sum(record)
s = Solution()
print(s.calPoints(["-9","-40","-35","D","73"]))


