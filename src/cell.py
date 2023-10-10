from IPython.display import clear_output


class Cell:
    '''Each Cell has:
        - Grid
        - Row 
        - Column
        - Nonant (Nine-quadrant)
    
    Each NineCell tells each of it's `Cells` that they can no longer be x,y, or z based on the other values in the Row, Column, or Nonant.
    The Cell itself has a 'solve_cell' function

    todo:
    each row and column of nonants produces abstract eliminations 

    Each Cell has a `position` in the 9x9 `SudokuGrid`
    
    Each Row, Column, and Nonant is numbered (1-9)

    '''


    def __init__(self,  grid, 
                        row,
                        column, 
                        nonant=None, 
                        value=None,
                        in_ink=False):
        
        self.symbols = [1,2,3,4,5,6,7,8,9]
        self.grid = grid

        ## position identifiers
        self.row = row
        self.row.cells.append(self)
        self.column = column
        self.column.cells.append(self)
        self.nonant = nonant    
        self.nonant.cells.append(self)
        self._value = value
        self._not_these = set()
        self.in_ink = in_ink

    @property
    def position(self):
        '''return an x,y coordinate for the cell on the 9x9 grid'''
        return (self.row.rownumber, self.column.colnumber)


    @property
    def impossible(self):
        return self._not_these

    @property
    def not_these(self):
        return self._not_these
    
    @not_these.setter
    def not_these(self, new):
        ''' when a cell has only one remaining potential value, fill it in'''
        self._not_these = new
        if len(new) == 8:
            self.solve_cell()


    @property
    def possible(self):
        if self.value == None:
            out = self.not_these.symmetric_difference(set([1,2,3,4,5,6,7,8,9]))

            ## this is the automatic solver thing
            # if len(out) == 1:
            #     self.value = list(out)[0]
                # self.solve_cell()
            return out
        else:
            return {self.value}

 
    @property
    def value(self):
        return self._value
            

    @value.setter
    def value(self, new):
        '''this function currently iterates the entire grid to eliminate the now-known value from their potential possibles'''
        self._value = new
        # print(f'solved {self.position} with {self._value} ')
        # print(f"Removing possibility for number {self.value} from Row {self.row.number}, Column {self.column.number}, and Block {self.nonant.number} because of a {self.value} in {self.position}")
        self.grid.show_grid
        for x in self.row.cells + self.column.cells + self.nonant.cells:

            if (x != self) and (x.value == None):
                if new not in x.not_these:
                    x.not_these.add(new)




    def solve_cell(self):
        # if cell.value is not None:
        #     return None
        #for x in self.row, self.column, self.nonant:
        #self.nonant.implied_axis_elimination()

        for name, y in zip(['Row', 'Column', 'Nonant'],[self.row.cells, self.column.cells, self.nonant.cells]):

            # make a copy
            sub_out = list([z for z in y if z != self])
            others = set()
            for j in [i.possible for i in sub_out]:
                others = others.union(j)


            if len(others) == 8:
                
                #choice = input(f"Do you want to impute {potential_answers} at {self.position}?")
                output = list(set([1,2,3,4,5,6,7,8,9]).difference(others))[0]
                self.value = output
                # print(f"solving cell {self.position} with {self.value}. {self.grid.total_trues} now solved.")
                print(f'Solving cell {self.position} with {self.value}. {name} elimination')
                return True

                ## this part for interactivity
                # if self.in_ink==False:
                #     # print(f'solving {self.position} after {type} elimination')
                #     display(self.grid)
                #     choice = input(f'Do you want to solve {self.position} with {output}')
                #     clear_output()
                #     if choice.casefold() in ['y', 'yes', 'ya']:
                #         self.value = output
                    
                #     elif choice.casefold() in ['quit', 'q', 'exit']:
                #         break
                #     else:
                #         pass



                #print(f"entered {self.value} at {self.position}")
                #self.nonant.implied_eliminations()
                #break
                # for x in [y:
                #     if x.value == None:
                #         x.solve_cell()
                #         x.nonant.implied_eliminations()
            # set(i.possible for i in sub_out)




    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return ""
            # return f"{self.position}"
            # return str(self.position)
        
