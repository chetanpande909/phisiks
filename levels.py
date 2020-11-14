'''
IDK if this is a gud way to do this but, it is the simplest :)
'''

from settings import WW, WH

'''
levelx[0] --> start position of a static line
levelx[1] --> end position of a static line
levelx[2] --> victory flag position
levelx[3] --> start position of the player
'''

level1 = [
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

level2 = [
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
