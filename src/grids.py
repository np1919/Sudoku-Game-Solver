
def hard_game(a):

    for k, v in {    4:4,
                    5:9,
                    6:6,
                    9:3,
                    11:4,
                    14:6,
                    15:1,
                    17:9,
                    19:2,
                    23:1,
                    25:3,
                    26:4,
                    28:1,
                    29:2,
                    32:4,
                    36:4,
                    39:5,
                    44:6,
                    46:8,
                    49:2,
                    50:9,
                    56:1,
                    57:6,
                    61:2,
                    66:9,
                    71:8,
                    73:6,
                    78:3,}.items():
        
        a.cells[k].value = v
    return None


def expert_game(a):
    for k, v in {4: 9,
                5: 1,
                6: 4,
                7: 3,
                12: 7,
                19: 7,
                22: 4,
                23: 5,
                25: 6,
                29: 3,
                30: 2,
                31: 5,
                32: 4,
                33: 1,
                35: 9,
                43: 2,
                44: 4,
                45: 4,
                50: 3,
                52: 8,
                53: 6,
                55: 6,
                56: 4,
                62: 1,
                64: 9,
                65: 8,
                66: 1,
                68: 2,
                69: 7,
                74: 2}.items():
                
        a.cells[k].value = v
    return None


def daily_2023_07_20(a):
     for k, v in {4:7, 6:8,8:1,
                19:7,21:4,22:3,23:5,
                38:5, 40:1, 41:2, 44:4,
                47:1, 50:9, 51:6, 53:5,
                54:7, 55:2, 56:4, 57:1,
                69:3,
                72:3, 75:5, 79:9}.items():
         a.cells[k].value = v






    ## hard game
    # a.cells[4].value=4
    # a.cells[5].value=9
    # a.cells[6].value=6
    # a.cells[9].value=3
    # a.cells[11].value=4
    # a.cells[14].value=6
    # a.cells[15].value=1
    # a.cells[17].value=9
    # a.cells[19].value=2
    # a.cells[23].value=1
    # a.cells[25].value=3
    # a.cells[26].value=4
    # a.cells[28].value=1
    # a.cells[29].value=2
    # a.cells[32].value=4
    # a.cells[36].value=4
    # a.cells[39].value=5
    # a.cells[44].value=6
    # a.cells[46].value=8
    # a.cells[49].value=2
    # a.cells[50].value=9
    # a.cells[56].value=1
    # a.cells[57].value=6
    # a.cells[61].value=2
    # a.cells[66].value=9
    # a.cells[71].value=8
    # a.cells[73].value=6
    # a.cells[78].value=3
    # return None