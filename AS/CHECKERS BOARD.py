import numpy as NP

def build_checkerboard(w, h) :
    re = NP.r_[ w*[0,1] ]
    ro = NP.r_[ w*[1,0] ]
    return NP.row_stack(h*(re, ro))


print(build_checkerboard(5, 5))

