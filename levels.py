'''
IDK if this is a gud way to do this but, it is the simplest :)
'''

from settings import WW, WH

'''
levelx[0] --> start position of a wall
levelx[1] --> end position of a wall
levelx[2] --> victory flag position
levelx[3] --> start position of the player
'''


level1 = [
    [
        (0, WH), (0, 0), (0, 0), (WW, 0), (WW//2-200, WH//2)
    ],
    [
        (WW, WH), (WW, 0), (0, WH), (WW, WH), (WW//2+200, WH//2)
    ],
    [
        (WW//2+100, WH//2-16)
    ],
    [
        (WW-100, WH-100)
    ]
]

level2 = [
    [
        (0, WH), (0, 0), (0, 0), (WW, 0), (0, 400), (400, 200)
    ],
    [
        (WW, WH), (WW, 0), (0, WH), (WW, WH), (400, 400), (WW, 200)
    ],
    [
        (WW-100, 190)
    ],
    [
        (WW-100, WH-100)
    ]
]


level3 = [
    [
        (0, WH), (0, 0), (0, 0), (WW, 0), (0, 100), (WW, 100), (0, 300), (WW, 300)
    ], 
    [
        (WW, WH), (WW, 0), (0, WH), (WW, WH), (WW//2-100, 200), (WW//2+100, 200), (WW//2-100, 400), (WW//2+100, 400)
    ], 
    [
        (WW-100, 100)
    ], 
    [
        (WW-100, WH-100)
    ]
]

level4 = [
    [
        (0, 0), (0, 0), (WW, 0), (WW, WH), (4*WW//5, WH), (0, 5*WH//6)
    ], 
    [
        (WW, 0), (0, WH), (WW, WH), (4*WW//5, WH), (4*WW//5, WH//2), (WW//2, WH)
    ], 
    [
        (50, 4.1*WH//5)
    ], 
    [
        (WW-100, WH-100)
    ]
]
## Keep this in the bottom and update it after adding a level
levels = [
    level1, level2, level3, level4
]