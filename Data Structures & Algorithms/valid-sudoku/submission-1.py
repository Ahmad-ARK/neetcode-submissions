# from collections import defaultdict

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = defaultdict(set)
#         cols = defaultdict(set)   
#         boxes = defaultdict(set) 

#         for r in range(9):
#             for c in range(9):
#                 val = board[r][c]

#                 if val == ".":
#                     continue
                
#                 box_id = (r // 3) * 3 + (c // 3)

#                 if val in rows[r] or val in cols[c] or val in boxes[box_id]:
#                     return False
                
#                 rows[r].add(val)
#                 cols[c].add(val)
#                 boxes[box_id].add(val)
#         return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                box_id = (r // 3) * 3 + (c // 3)

                if val in rows.get(r, set()) or val in cols.get(c, set()) or val in boxes.get(box_id, set()):
                    return False
                
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if box_id not in boxes:
                    boxes[box_id] = set()
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True