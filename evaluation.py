"""
This module evaluates AI agents in a 8x8 board. Different board states with optimal moves (as solutions) are given as test cases. 
* The agent is evaluated based on attack performance, defense performance, and intelligence. 
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
    'solution': [(2,4), (2,0)]
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
        [None, 'O' , 'X' , 'X' , None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'O' , 'X' , None, None, None, None],
        [None, None, 'O' , 'O' , 'X' , None, None, None],
        [None, None, 'O' , None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,1), (6,5)]
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
    'solution': [(4,0)]
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
    'solution': [(6,1)]
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
        ['X' , None, 'O' , 'O' , 'O' , None, None, None],
        [None, 'X' , 'O' , 'O' , None, None, None, None],
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
    
    #15
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
    
    #16
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
    
    #17
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, 'O' ],
        [None, None, None, None, None, None, 'X' , None],
        [None, None, None, None, 'O' , 'X' , 'X' , None],
        [None, None, None, None, 'O' , 'X' , None, 'O' ],
        [None, None, None, None, 'O' , 'X' , None, None],
        [None, None, None, None, None, 'X' , None, None],
    ],
    'solution': [(3,5)]
    },
    
    #18
    {
    'board': [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, 'O' , 'O' , None],
        [None, None, None, None, None, 'X' , 'X' , 'X' ],
        [None, None, None, None, 'X' , None, None, None],
        [None, 'O' , None, None, None, 'X' , None, None],
        [None, 'O' , None, 'O' , None, None, 'X' , None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(3,4)]
    },
    
    #19
    {
    'board': [
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, 'X' , 'X' , 'X' , None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , None, None, None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(1,2)]
    },
    
    #20
    {
    'board': [
        [None, None, 'X' , 'O' , None, None, None, None],
        [None, None, 'O' , 'X' , 'X' , 'X' , None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'X' , None, 'X', None, None],
        [None, 'O' , 'X' , 'O' , None, None, None, None],
        [None, None, None, 'O' , 'O' , None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ],
    'solution': [(2,4)]
    },
]

intelligence_testcase = [
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
    'solution': [(4,2)]
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
        [None, 'O' , 'X' , 'X' , None, None, None, None],
        [None, None, 'X' , 'O' , None, None, None, None],
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
    'solution': [(4,4)]
    },
]

def write(content, file, export=True):
    if export: print(content)
    with open(file, 'a') as f:
        f.write(content + '\n')

if __name__=='__main__':
    # Initialize Argument Parser for command line arguments
    import argparse
    import os
    from project import Player, Game
    
    parser = argparse.ArgumentParser(description='Evaluation of Gomoku player.')
    parser.add_argument('--player', '-p', required=True, type=str, default='intermediate', help='Choose the agent to evaluate')
    parser.add_argument('--load', '-l', type=str, default=None, help='Load weight file for Tabular/Approximate Q-Learning Player')
    parser.add_argument('--no_train', action='store_true', help='No training for Q-Learning Player')
    args = parser.parse_args()

    args.game = 'gomoku'
    args.size = 8
    game = Game(args)

    attack_player = Player(args, player=args.player, letter='X')
    defense_player = Player(args, player=args.player, letter='O')

    if args.load:
        if not args.load.startswith('8x8'):
            invalid_size = args.load.split('_')[0]
            raise ValueError(f'The weight file is used for {invalid_size} board, but the board for evaluation is 8x8. Please use the weight file for 8x8 board.')

    if 'Q-Learning' in str(attack_player):
        if args.load is not None:
            attack_player.load_weight(args.load) 
        if args.no_train == False:
            attack_player.train(game)

    if 'Q-Learning' in str(defense_player):
        if args.load is not None:
            defense_player.load_weight(args.load)
        if args.no_train == False:
            defense_player.train(game)

    output =f"evaluation/{args.player}.txt"
    os.makedirs(os.path.dirname(output), exist_ok=True)
    open(output, 'w').close() # Clear the output files

    # Attack testcases
    attack_corrects = 0

    write(f"Evaluting {str(attack_player).capitalize()} player", output)
    
    write("----- Attack -----", output)
    
    def get_random_lastmove(board, letter):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == letter:
                    return (i, j)
                
    for i, testcase in enumerate(attack_testcase):
        # Restart if the player is Master Player
        if hasattr(attack_player, 'restart') and callable(getattr(attack_player, 'restart')):
            attack_player.restart()

        board = testcase['board']
        solution = testcase['solution']
        game.board_state = board
        game.last_move = get_random_lastmove(game.board_state, 'O')
        game.curr_player = 'X'

        move = tuple(attack_player.get_move(game))

        if move in solution:
            write(f'Test {i+1}: Passed', output)
            attack_corrects += 1
        else:
            write(f'Test {i+1}: Failed', output)
            index_str = " "
            for i in range(len(board[0])):
                index_str += "  " + str(i) 
            write(index_str, output, export=False)

            for i in range(len(board[0])):
                content = f"{i}"
                row = board[i]
                for c in row:
                    if c == 'X' or c == 'O':
                        content += "  " + c
                    else:
                        content += "  " + "-"
                write(content, output, export=False)
            write(f"Player's move: {move}", output, export=False)
            write(f"Optimal  move: {solution}", output, export=False)

    defense_corrects = 0
    
    write("----- Defense -----", output)

    for i, testcase in enumerate(defense_testcase):
        # Restart if the player is Master Player
        if hasattr(defense_player, 'restart') and callable(getattr(defense_player, 'restart')):
            defense_player.restart()

        board = testcase['board']
        solution = testcase['solution']
        game.board_state = board
        game.last_move = get_random_lastmove(game.board_state, 'X')
        game.curr_player = 'O'

        move = tuple(defense_player.get_move(game))

        if move in solution:
            write(f'Test {i+1}: Passed', output)
            defense_corrects += 1
        else:
            write(f'Test {i+1}: Failed', output)
            index_str = " "
            for i in range(len(board[0])):
                index_str += "  " + str(i) 
            write(index_str, output, export=False)

            for i in range(len(board[0])):
                content = f"{i}"
                row = board[i]
                for c in row:
                    if c == 'X' or c == 'O':
                        content += "  " + c
                    else:
                        content += "  " + "-"
                write(content, output, export=False)
            write(f"Player's move: {move}", output, export=False)
            write(f"Optimal  move: {solution}", output, export=False)

    intelligence_corrects = 0
    
    write("----- Intelligence -----", output)

    for i, testcase in enumerate(intelligence_testcase):
        # Restart if the player is Master Player
        if hasattr(attack_player, 'restart') and callable(getattr(attack_player, 'restart')):
            attack_player.restart()

        board = testcase['board']
        solution = testcase['solution']
        game.board_state = board
        game.last_move = get_random_lastmove(game.board_state, 'O')
        game.curr_player = 'X'

        move = tuple(attack_player.get_move(game))

        if move in solution:
            write(f'Test {i+1}: Passed', output)
            intelligence_corrects += 1
        else:
            write(f'Test {i+1}: Failed', output)
            index_str = " "
            for i in range(len(board[0])):
                index_str += "  " + str(i) 
            write(index_str, output, export=False)

            for i in range(len(board[0])):
                content = f"{i}"
                row = board[i]
                for c in row:
                    if c == 'X' or c == 'O':
                        content += "  " + c
                    else:
                        content += "  " + "-"
                write(content, output, export=False)
            write(f"Player's move: {move}", output, export=False)
            write(f"Optimal  move: {solution}", output, export=False)

    write('-------------------', output)

    total_corrects = attack_corrects + defense_corrects + intelligence_corrects
    totals = len(attack_testcase) + len(defense_testcase) + len(intelligence_testcase)
    write(f"Attack: {attack_corrects}/{len(attack_testcase)}", output)
    write(f"Defense: {defense_corrects}/{len(defense_testcase)}", output)
    write(f"Intelligence: {intelligence_corrects}/{len(intelligence_testcase)}", output)
    write(f"Total: {total_corrects}/{totals}", output)
    

