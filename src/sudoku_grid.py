
import pandas as pd
import numpy as np
from .cell import Cell
from .grids import hard_game, expert_game
from .nine_cell import Row, Column, Nonant










class SudokuGrid:
    
    def __init__(self):

        # if cells == None:

        # # nonants

        # make the grid
        self.cells = []
        self.rows = [Row(self, x) for x in range(1,10)] 
        self.columns = [Column(self, x) for x in range(1,10)]
        self.nonants = [Nonant(self, x) for x in range(1,10)]

        for x in self.rows:
            for y in self.columns:
                # assigning nonant
                #self.cells.append(Cell(self, row=x, column=y))
                
                if x.rownumber >= 7:
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[8]))
                    elif (y.colnumber <= 6) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[7]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[6]))


                if (x.rownumber <= 6 ) and (x.rownumber >= 4):
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[5]))
                    elif (y.colnumber <= 6 ) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[4]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[3]))


                if x.rownumber <= 3:
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[2]))
                    elif (y.colnumber <= 6) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[1]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[0]))

        for ninecell in self.rows + self.columns + self.nonants:
            ninecell.grid = self
        
        
    
    @property
    def show_grid(self):
        '''for easy visual inspection..'''
        #print(self.total_trues)
        out= pd.DataFrame(np.array(self.cells).reshape(9,9), index=range(1,10), columns=range(1,10))
        out.index = ["*" for x in out.index]
        out.columns = ["*" for x in out.columns]
        print(out)
        #return out


    @property
    def total_trues(self):
        return sum([1 for x in self.cells if x.value is not None])
    
    @property
    def show_untrues(self):
        data = [len(x.not_these) if x.value == None  else "" for x in self.cells]
        return pd.DataFrame(np.array(data).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def show_possibles(self):
        return pd.DataFrame(np.array([x for x in self.possibles]).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def possibles(self):
        return [x.possible if x.value == None else set() for x in self.cells ] 

        # return [x.not_these.symmetric_difference(set([1,2,3,4,5,6,7,8,9])) if x.value == None else x.value for x in self.cells] 
    
    @property
    def show_impossibles(self):
        return pd.DataFrame(np.array([x for x in self.impossibles]).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def impossibles(self):
        return [x.not_these if x.value == None else set() for x in self.cells] 
    
    @property
    def show_nonants(self):
        return pd.DataFrame(np.array([x.nonant.nonant for x in self.cells]).reshape(9,9), index=range(1,10), columns=range(1,10))


    # def show_blocked(self, number):
    #     data = []
    #     for x in self.cells:
    #         if x.value == None:
    #             if number in x.not_these:
    #                 data.append(number)
    #             else:
    #                 data.append(x.position)
    #         else:
    #             data.append(x.value)
    #     return pd.DataFrame(np.array(data).reshape(9,9), index=range(1,10), columns=range(1,10))

    # def show_wanted(self, number):
    #     data = []
    #     for x in self.cells:
    #         if x.value == None:
    #             if number not in x.not_these:
    #                 data.append(number)
    #             else:
    #                 data.append('')
    #                 #data.append(x.position)
    #         else:
    #             data.append('')
    #             # data.append(x.value)

    #     return pd.DataFrame(np.array(data).reshape(9,9), index=range(1,10), columns=range(1,10))

    # def show_pressure(self, number):
    #     data = [number if number in x.not_these else x for x in self.cells]
    
    
    def __repr__(self):
        return str(self.show_grid)
    

    def setup(self):
        for k,v in load_game().items():
            self.cells[k].value = v
            self.cells[k].in_ink = True

    def solve(self):
        while self.total_trues != 81:                
            for _ in [_ for _ in self.cells if _.value is None]:
                    solved = _.solve_cell()
                    # if solved == True:
                    if solved == True:
                        for x in _.row.cells + _.column.cells + _.nonant.cells:

                            if x.value is None:
                                x.solve_cell()
            # print(self.total_trues)

    
    # def make_random(self):
    #     import random 

    #     random.shuffle(self.cells)
    #     for x in self.cells:
            
if __name__ == '__main__':
    a=SudokuGrid()
    hard_game(a)
    a.show_grid
    # a.show_nonants
    # a.show_possibles
    # a.len_untrues
    # a.trues