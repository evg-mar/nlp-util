# -*- coding: utf-8 -*-
"""
@author: evgeniy

Implementation of the Levenstein and Edit distances.
Levenstein: remove + add = exchange of a letter costs 2
Edit:       remove + add = exchange of a letter costs 1
"""

import numpy as np

#dummy value for the Levenstein/Edit distance matrix
dummyval = -1

def strDistance(str01, str02, distType, methodvalues=None):
    """
    strDistance implements the generalized case of
    Levenstein and Edit distances through the distType boolean argument.
    A recursive call of strDistances is done in def check_return.
    """
    ad = 2 if (distType == "levenstein") else 1

    l01, l02 = len(str01), len(str02)
    if(methodvalues is None):
        methodvalues = np.full((len(str01)+1, len(str02)+1), 
                               dummyval, 
                               dtype=np.int)
        methodvalues[0,:l02+1] = list(range(0, l02+1))        
        methodvalues[:l01+1,0] = list(range(0, l01+1))   
                        
    if l01 == 0:
        return l02
    elif l02 == 0:
        return l01
    else:
        
        def check_return(idx01, idx02, ad0):
            if(methodvalues[idx01, idx02] != dummyval):
                return methodvalues[idx01, idx02] + ad0
            else:
                # recursive call
                result =  strDistance(str01[:idx01], str02[:idx02],
                                  distType, methodvalues) + ad0
                # methodvalues[idx01, idx02] = result
                return result

        if str02[-1] == str01[-1]:
            res = check_return(l01-1, l02-1, 0)
            methodvalues[l01,l02] = res
            return res
        else:
            diag = check_return(l01-1, l02-1, ad)
            left = check_return(l01-1, l02, 1)
            right = check_return(l01, l02-1, 1)
            res = min(diag, left, right)
            methodvalues[l01,l02] = res
            return res


def LevensteinDistance(str01, str02):
    """
    Define the Levenstein distance:
    remove + add = exchange of a letter costs 2
    """
    return strDistance(str01, str02, "levenstein")

    
def EditDistance(str01, str02):
    """
    Define the Edit distance:
    remove + add = exchange of a letter costs 1
    """
    return strDistance(str01, str02, "edit")

###################################################
#############  Define  TESTS  #####################
###################################################

test_list = [
(('gresl', 'goejl'),(4,2)),
(('lara', 'som'),(4,2)),
]

def TestDistances(test_list):
    for (str01,str02), (leven, edit) in test_list:
        leven_result = LevensteinDistance(str01, str02)        
        if leven_result != leven:
            print('Levenstein computed {0:3d}, test value: {1:3d}'
                .format(leven_result,leven))
        edit_result = EditDistance(str01, str02)        
        if edit_result != edit:
            print('Edit computed {0:3d}, test value: {1:3d}'
                .format(edit_result,edit))

    
 
TestDistances(test_list)

                       