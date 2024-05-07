"""
This module evaluates AI agents in a 8x8 board. Different board states with optimal moves (as solutions) are given as test cases. 
* The agent is evaluated based on attack performance, defense performance, and creative performance. 
* The agent is expected to make (one of) optimal moves in each state.
! Note 1: Since these test cases are hand-crafted, there may contain errors in the solutions. Please let me know if you find any errors.
! Note 2: The evaluation could take a long time to run if your agent is not efficient.
"""
# Empty 8x8 board
empty_board = [
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
]

attack_testcase = [
    # *Test cases that look for obvious move(s) that result in a win. You move with [X].
    
    #1
    {
    'board': [
        ['O' , 'X' , 'X' , 'X' , 'X' , None, None, None],
        ['O' , 'O' , 'O' , 'O' , 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(0,5)]
    },
    
    #2
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['X' , 'O' , 'O' , 'O' , 'O' , None, None, None],
        ['X' , None, 'O' , 'O' , None, None, None, None],
        ['X' , 'X' , 'X' , 'X' , 'O' , None, None, None],
        ['X' , None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(0,0), (5,0)]
    },
    
    #3
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , 'X' , None, 'O' , None, None, None, None],
        [None, None, None, 'O' , None, None, 'O' , None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, 'X' , 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(7,1)]
    },
    
    #4
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , 'X' , 'O' , 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, 'X' , None, 'O' , None, None],
        [None, None, 'X' , 'O' , 'X' , None, None, None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, 'X' , None, None, None, 'X' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(7,7)]
    },
    
    #5
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, 'X' , 'X' , 'X' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, 'O' , 'O' , 'O' , None, None],
        [None, None, None, 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, 'O' , 'X' , 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(6,6)]
    },
    
    #6
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , None, None, 'X' , None, None],
        [None, None, 'O' , None, 'X' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
    ],
    'solution': [(6,2)]
    },
    
    #7
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, None, 'O' , None],
        ['O' , 'X' , None, 'X' , 'X' , 'X' , 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,2)]
    },
    
    #8
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['X' , None, 'O' , 'O' , 'O' , 'O' , None, None],
        [None, 'X' , 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, 'X' , 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,2)]
    },
    
    #9
    {
    'board': [
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , 'O' , None, 'X' , None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
    ],
    'solution': [(4,2)]
    },
    
    #10
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, 'O' ],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , 'X' , None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, 'O' , None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #11
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
        [None, None, 'O' , None, 'O' , None, None, None],
        [None, None, None, 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , 'O' , None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #12
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , 'X' , 'X' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, 'O' , None, None, None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,4)]
    },
    
    #13
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,1), (6,5)]
    },
    
    #14
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, 'O' , 'X' , None, None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,5), (5,5)]
    },
    
    #15
    {
    'board': [
        [None, None, None, None, None, None, None, 'X' ],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, 'O' , None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, None, None, 'O' , None, None, None, None],
        [None, None, None, 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,2)]
    },
    
    #16
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, 'O' , None, None],
        [None, None, 'X' , 'X' , None, 'X' , None, None],
        [None, None, None, 'O' , None, 'O' , None, None],
        [None, None, 'O' , None, 'X' , 'X' , None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,4)]
    },
    
    #17 
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, None, None, None, 'O' , None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,3)]
    },
    
    #18 
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , 'X' , None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, None, None , None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, None, 'O' , 'O', 'O' , None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,3)]
    },
    
    #19
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, None, None, 'O' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #20
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
        [None, 'X' , 'O' , "O" , "O" , 'X' , None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, 'X' , None, 'O' , None, 'X' , None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,1)]
    },
    
    #21
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None , None, None, None, None, None, None],
        [None, None , 'O' , "O" , "O" , 'O' , 'X', None],
        [None, 'X' , None, None, 'O' , None, None, None],
        [None, 'X' , None, None, None, 'X' , None, None],
        [None, 'X' , None, None, 'X' , 'O' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,1)]
    },
    
    #22
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , "X" , "O" , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , 'X' , 'X' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,3)]
    },
    
    #23
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , "X" , "X" , None, None, None],
        [None, None, 'O' , None, 'X' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, 'X' , 'O' , 'X' , None],
        [None, None, None, None, None, None, None, 'X' ],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,5)]
    },
    
    #24
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , 'X' , 'X' , None, None, None],
        [None, None, 'O' , None, 'X' , None, None, None],
        [None, None, 'O' , 'O' , 'O' , None, 'O' , None],
        [None, None, None, None, 'X' , 'O' , 'X' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,5)]
    },
    
    #25
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, None, 'O' , 'O' , 'O' ],
        [None, None, None, 'X' , None, 'O' , 'O' , None],
        [None, None, None, 'X' , 'X' , 'O' , 'O' , None],
        [None, None, None, 'X' , None, 'X' , 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(6,6)]
    },
    
    #26
    {
    'board': [
        [None, None, None, None, 'O' , 'O' , 'O' , 'O' ],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'X' , None, None, 'O' , None],
        [None, None, None, 'X' , 'X' , None, 'O' , None],
        [None, None, None, 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, None, None, None, 'O'],
    ],
    'solution': [(2,2)]
    },
    
    #27
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , None, None, None, None, None, None, None],
        ['O' , 'X' , None, None, None, None, 'X' , None],
        ['O' , None , 'X', None, None, 'O' , None, None],
        [None, 'O' , 'O' , 'X' , 'O' , None, None, None],
        ['O' , 'X' , 'X' , 'X' , 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(6,5), (5,5)]
    },
    
    #28
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , None, None, None, None, None, None, 'X' ],
        ['O' , 'X' , None, None, None, None, 'X' , None],
        ['O' , None, 'X' , None, None, None, None, None],
        ['O' , 'O' , 'O' , 'O' , 'X' , None, None, None],
        ['X' , 'X' , 'X' , 'X' , 'O' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #29
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        ['O' , 'X' , None, None, None, None, None, None],
        ['O' , None, 'X' , None, None, None, None, None],
        ['O' , 'O' , 'O' , 'X' , None, None, None, None],
        ['O' , 'X' , 'X' , 'X' , 'X' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,0), (6,5), (5,5)]
    },
    
    #30
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, 'O' , None, 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, 'O' , 'O' , 'X' , None, None, None, None],
        [None, None, 'O' , 'O' , 'X' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,6), (2,1), (6,5)]
    },
]

defense_testcase = [
    # *Test cases that look for defensive move(s) that prevent the opponent from winning. You move with [O]
    
    #1
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, 'X' ],
        ['O' , 'X' , None, None, None, None, 'X' , None],
        ['O' , 'O' , 'X' , None, None, None, None, None],
        ['O' , 'O' , 'O' , 'O' , 'X' , None, None, None],
        ['X' , 'X' , 'X' , 'X' , 'O' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #2
    {
    'board': [
        ['O' , 'X' , 'X' , 'X' , 'X' , None, None, None],
        ['O' , 'O' , 'O' , 'O' , 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(0,5)]
    },
    
    #3
    {
    'board': [
        ['X' , None, 'O' , 'O' , None, None, None, None],
        ['X' , None, 'O' , 'O' , None, None, None, None],
        ['X' , None, 'O' , 'O' , None, None, None, None],
        ['X' , 'X' , 'X' , None, None, None, None, None],
        [None , None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,0)]
    },
    
    #4
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , 'X' , None, 'X' , None, None, None, None],
        [None, None, None, 'O' , None, None, 'O' , None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, 'O' , 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(7,1)]
    },
    
    #5
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , 'X' , 'O' , 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, 'X' , None, 'O' , None, None],
        [None, None, 'X' , 'O' , 'X' , None, None, None],
        [None, None, None, 'O' , None, 'X' , None, None],
        [None, None, 'X' , None, None, None, 'X' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(7,7)]
    },
    
    #6
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, 'X' , 'X' , 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, 'O' , 'X' , 'O' , None, None],
        [None, None, None, 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'X' , 'X' , 'X' , 'X' , 'O' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(6,6)]
    },
    
    #7
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , 'O' , None, 'X' , None, None],
        [None, None, 'O' , None, 'X' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
    ],
    'solution': [(6,2)]
    },
    
    #8
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, None, 'O' , None],
        ['O' , 'X' , None, 'X' , 'X' , 'X' , 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,2)]
    },
    
    #9
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['X' , None, 'O' , 'O' , 'O' , 'O' , None, None],
        [None, 'X' , 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, 'X' , 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,2)]
    },
    
    #10
    {
    'board': [
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , 'O' , None, 'X' , None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
    ],
    'solution': [(4,2)]
    },
    
    #11
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, 'O' ],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , 'X' , None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, 'O' , None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #12
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
        [None, None, 'O' , None, 'O' , None, None, None],
        [None, None, None, 'O' , 'X' , None, None, None],
        [None, None, None, 'X' , 'O' , None, None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, 'X', None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #13
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , 'X' , 'X' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, 'O' , 'O' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,1), (2,5)]
    },
    
    #14
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,1), (6,5)]
    },
    
    #14
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, 'O' , 'X' , None, None],
        [None, None, None, 'O' , 'O' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,5), (5,5)]
    },
    
    #15
    {
    'board': [
        [None, None, None, 'O' , None, None, None, None],
        [None, None, None, None, 'O' , None, None, None],
        [None, 'X' , None, None, 'O' , 'O' , None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , None, 'X' , None, None, None],
        [None, 'X' , None, None, None, None, None, None],
        ['X' , None, None, None, None, None, None, None],
    ],
    'solution': [(4,3)]
    },
    
    #16
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , None, 'O' ],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, 'O' , 'X' , 'X' , None],
        [None, None, None, None, None, 'X' , 'O' , 'O' ],
        [None, None, None, None, None, 'X' , 'O' , None],
        [None, None, None, None, None, 'X', None, None],
    ],
    'solution': [(4,4)]
    },
    
    #17
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , 'O' , None],
        [None, None, None, None, None, 'X' , 'X' , 'X' ],
        [None, None, None, None, 'X' , None, None, None],
        [None, 'O' , None, None, None, 'X' , None, None],
        [None, 'O' , None, 'O' , None, None, 'X' , None],
        [None, None, 'O' , None, None, None, None, None],
    ],
    'solution': [(3,4)]
    },
    
    #18
    {
    'board': [
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, 'X' , 'X' , 'X' , None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, 'O' , 'X' , 'O' , None, None, None, None],
        [None, 'O' , None, 'O' , 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,3)]
    },
    
    #19
    {
    'board': [
        [None, None, 'X' , 'O' , 'O' , None, None, None],
        [None, None, None, 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'X' , None, 'X', None, None],
        [None, 'O' , 'X' , 'O' , None, None, None, None],
        [None, 'O' , None, 'O' , 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,4)]
    },
    
    #20
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, 'X' , 'O' , 'O' , None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,5), (5,1)]
    },
]

creative_testcase = [
    # *Test cases that look for intelligent but hard-to-find move(s) that result in a win. You move with [X].
    
    #1
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, None, 'O' , None, 'O' ],
        [None, None, None, 'X' , None, 'X' , 'O' , None],
        [None, None, None, None, None, 'O' , 'X' , None],
        [None, None, None, 'X' , None, 'X' , 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,4)]
    },
    
    #2
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , None, 'O' ],
        [None, 'X' , 'X' , 'O' , None, 'O' , 'X' , None],
        [None, None, None, None, None, 'X' , 'X' , 'O' ],
        [None, None, 'X' , 'X' , None, 'O' , 'O' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,2)]
    },
    
    #3
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'O' , None, None, None, 'O' , None],
        [None, 'O' , 'O' , 'X' , None, 'X' , None, None],
        [None, None, 'X' , None, 'X' , None, None, None],
        [None, None, 'O' , 'X' , None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, 'O' , None, None, None, None, None, None],
    ],
    'solution': [(4,3)]
    },
    
    #4
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'O' , 'X' , None, None, None, None, None],
        [None, 'O' , 'X' , None, None, None, None, None],
        [None, None, None, 'X' , 'X' , None, None, None],
        [None, None, None, 'O' , 'O', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(4,2)]
    },
    
    #5
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , 'O' , 'X' , None, None, None],
        [None, 'X' , None, 'O' , None, 'X' , None, None],
        [None, None, None, 'O' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,3)]
    },
    
    #6
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , None , 'X', None, None, None],
        [None, 'O' , None, 'X' , 'O' , 'O' , None, None],
        [None, None, None, 'X' , None, None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,3)]
    },
    
    #7
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, 'O' , 'O' , None, None, None, None, None],
        [None, 'X' , 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,4)]
    },
    
    #8
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'O' , None],
        [None, None, None, 'X' , None, None, 'O' , None],
        [None, None, None, 'X' , 'O' , 'X' , 'O', None],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,3)]
    },
    
    #9
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , None, None],
        [None, 'O' , 'X' , 'X' , 'O' , None, None, None],
        [None, None, 'X' , 'O' , 'X' , None, None, None],
        [None, None, None, None, None, 'O' , None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,2)]
    },
    
    #10
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, 'X' , 'X' , None, None],
        [None, None, None, None, 'O' , 'O' , 'X' , None],
        [None, None, None, None, 'O' , 'O' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,6)]
    },
    
    #11
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , None, None, None, None, None, None, None],
        [None, 'X' , None, None, None, None, 'X' , None],
        [None, 'O' , 'X' , None, None, 'O' , None, None],
        [None, 'O' , 'O' , 'X' , 'O' , None, None, None],
        ['O' , 'X' , 'X' , 'X' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,4)]
    },
    
    #12
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        ['O' , None, None, None, None, None, None, None],
        [None, 'O' , None, None, None, None, None, None],
        [None, 'O' , 'X' , 'X' , None, 'O' , None, None],
        [None, 'O' , 'O' , 'X' , 'O' , None, None, None],
        ['X' , 'X' , 'X' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,3)]
    },
    
    #13
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , 'O' , 'O' ],
        [None, None, None, None, None, 'O' , 'O' , 'O' ],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'X' , 'X' , 'X' ],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, None, 'X' , None, None],
        [None, None, None, None, None, None, 'X' , None],
    ],
    'solution': [(4,3)]
    },
    
    #14
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, 'X' , None, 'O' , None, None, None],
        [None, None, 'O' , 'X' , 'O' , None, None, None],
        [None, None, None, None, None, 'X' , 'X' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,4)]
    },
    
    #15
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, 'X' , 'X' , 'O' , None],
        [None, None, 'O' , 'X' , 'O' , 'X' , None, None],
        [None, None, 'O' , 'X' , 'O' , 'O' , None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, None, None, None, None, 'X' , None, None],
    ],
    'solution': [(2,3)]
    },
    
    #16
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X',  'O' , None, 'O' , None, None],
        [None, None, None, 'X' , 'X' , 'X' , 'O' , None],
        [None, None, 'X' , None, 'O' , 'O' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,2)]
    },
    
    #17
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, None, None, 'O',  'O' , None, None],
        [None, None, 'X' , None, 'X' , 'O' , 'O' , None],
        [None, 'X' , None, None, None, None, 'X' , None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,3)]
    },
    
    #18
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, 'O' , None, 'O' , 'O' , None, None],
        [None, None, 'X' , None, 'X' , None, None, None],
        [None, 'X' , None, None, 'O' , 'X' , None, None],
        ['X' , None, None, None, None, None, 'O' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,3)]
    },
    
    #19
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'O' , 'X' , 'X' , None, None],
        [None, None, None, 'X' , 'O' , 'X' , None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,5)]
    },
    
    #20
    {
    'board': [
        [None, None, None, None, 'X' , None, None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, None, None, None, 'X' , 'O' , None, None],
        [None, None, None, None, None, 'O' , None, None],
        ['X' , 'X' , 'X' , None, None, None, None, None],
        [None, 'O' , 'O' , 'O' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(5,5)]
    },
]

def eval():
    print("Eva")

if __name__=='__main__':
    # Initialize Argument Parser for command line arguments
    import argparse
    
    parser = argparse.ArgumentParser(description='Play Tic Tac Toe or Gomoku')
    parser.add_argument('--game', '-g', type=str, default='tictactoe', choices=['tictactoe', 'gomoku'], help='Choose the game to play (tictactoe or gomoku)')
    parser.add_argument('--player1', '-p1', type=str, default='random', help='Choose player 1')
    parser.add_argument('--player2', '-p2', type=str, default='human', help='Choose player 2')
    parser.add_argument('--mode', '-m', type=str, default='plain', choices=['silent', 'plain', 'ui'], help='Choose visualization mode')
    parser.add_argument('--num_games', '-n', type=int, default=1, help='Number of games to run')
    parser.add_argument('--timeout', '-t', type=int, default=5, help='Timeout for each move')
    args = parser.parse_args()