from itertools import chain


### Parent Class

class NineCell():
    ''' each nonant is a group of 9 cells. '''
    def __init__(self, grid):
        self.cells = []
        self._known_cells = set()
        self.grid = grid

    @property
    def possibles(self):
        return [x.not_these.difference(set([1,2,3,4,5,6,7,8,9])) if x.value == None else x.value for x in self.cells] 
    
### Child Classes

class Row(NineCell):
    '''inherits the cells list, the possibles method, and the instance of SudokuGrid from NineCell'''
    def __init__(self, grid, rownumber,):
        NineCell.__init__(self, grid)
        self.rownumber = rownumber
        self.number = rownumber
    # def __repr__(self):
    #     return f"Row {self.rownumber}"
    

class Column(NineCell):
    '''inherits the cells list, the possibles method, and the instance of SudokuGrid from NineCell'''
    def __init__(self, grid, colnumber):
        NineCell.__init__(self, grid)
        self.colnumber = colnumber
        self.number = colnumber
    # def __repr__(self):
    #     return f"Column {self.colnumber}"
    

class Nonant(NineCell):
    '''inherits the cells list, the possibles method, and the instance of SudokuGrid from NineCell'''
    def __init__(self, grid, nonant):
        NineCell.__init__(self, grid)
        self.nonant = nonant
        self.number = nonant

    def implied_axis_elimination(self):
        '''nested function to imply linear elimination based on the other cells in this nonant'''

        row_combos = [self.cells[:3],self.cells[3:6], self.cells[6:10]]
        column_combos = [[self.cells[0],self.cells[3], self.cells[6]],
                        [self.cells[1],self.cells[4],self.cells[7]],
                        [self.cells[2], self.cells[5], self.cells[8]]]
        
        def return_comparison_sets(combo):
            '''determine the unique possible values in each row and column
            accepts a list of 3 lists...
            returns a list of 3 sets'''
            out = []
            for row in combo:
                temp = set()
                for x in row:
                    temp = temp.union(x.possible)
                out.append(temp)
            return out
        
        def compare_sets(three_sets):
            '''compare the unique values for each row or column to the other two to determine an implied linearity
            
            accepts a list of three sets
            return a list of three sets'''
            output = []
            for idx, x in enumerate(three_sets):
                # print(x)
                temp = three_sets.copy()
                current = temp.pop(idx)
                temp = temp[0].union(temp[1])
                diff = current.difference(temp)
                # print(current, temp, diff)
                output.append(diff)
            # yield diff
            return output
        
        def implement_eliminations():
            '''modify the cells along each row or column based on the implied linear elimination from this nonant'''
            for row, possibles in zip(row_combos, compare_sets(return_comparison_sets(row_combos))):
                # print(f'{row[0].row} outside nonant {self.number} must not contain {possibles}')
                for x in row[0].row.cells:
                    if x not in self.cells:
                        x.not_these = x.not_these.union(possibles)
            for column, possibles in zip(column_combos, compare_sets(return_comparison_sets(column_combos))):
                # print(f'{column[0].column} outside nonant {self.number} must not contain {possibles}')
                for x in column[0].column.cells:
                    if x not in self.cells:
                        x.not_these = x.not_these.union(possibles)
        
        implement_eliminations()











    ### each nonant should be able to check whether certain values are contained within one of their cells.


    #     self.verticals = [[],[],[]]
    #     self.horizontals = []

    # def assign_laterals(self):
        
    #     for idx, (x,y) in enumerate(zip([0,3,6], [3,6,9])):
    #         self.horizontals.append(self.cells[x:y])

    #     for idx, values in enumerate([[0,3,6], [1,4,7], [2,5,8]]):
    #         for y in values:
    #             self.verticals[idx] += [self.cells[y]]

    
    # def check_laterals(self):
    #     result = set([x.possible for x in self.verticals[0]]).difference(set([x.possible for x in self.verticals[1]]).union([x.possible for x in self.verticals[2]]))
    #     print(result)
    

             #   others = set(chain.from_iterable([x.possible for x in second_temp]))


    def __repr__(self):
        return f"Nonant {self.nonant}"
