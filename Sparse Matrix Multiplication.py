# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:59:57 2022

@author: patzo
"""
def sparse_matrix(base_type=float):
    """Returns a sparse matrix using nested default dictionaries."""
    from collections import defaultdict
    return defaultdict(lambda: defaultdict (base_type))

def vector_keyed(keys=None, values=0, base_type=float):
    if keys is not None:
        if type(values) is not list:
            values = [base_type(values)] * len(keys)
        else:
            values = [base_type(v) for v in values]
        x = dict(zip(keys, values))
    else:
        x = {}
    return x


# Test cell: `spmv_keyed_test`

#   'row':  / 0.   -2.5   1.2 \   / 1. \   / -1.4 \
#  'your':  | 0.1   1.    0.  | * | 2. | = |  2.1 |
#  'boat':  \ 6.   -1.    0.  /   \ 3. /   \  4.0 /

KEYS = ['row', 'your', 'boat']

A_keyed = sparse_matrix()
A_keyed['row']['your'] = -2.5
A_keyed['row']['boat'] = 1.2
A_keyed['your']['row'] = 0.1
A_keyed['your']['your'] = 1.
A_keyed['boat']['row'] = 6.
A_keyed['boat']['your'] = -1.

x_keyed = vector_keyed (KEYS, [1, 2, 3])
y0_keyed = vector_keyed (KEYS, [-1.4, 2.1, 4.0])

#print(x_keyed)
#print(y0_keyed)
#print(A_keyed.items())

def spmv_keyed(A, x):
    """Performs a sparse matrix-vector multiply for keyed matrices and vectors."""
    assert type(x) is dict
    
    y = vector_keyed(keys=A.keys(), values=0.0)
    
    for i,row_i in A.items():
        s=0.
        for j,a_ij in row_i.items():
          s+=a_ij*x[j]
          y[i]=s
    return y

# Try your code:
y_keyed = spmv_keyed (A_keyed, x_keyed)

# Measure the residual:
residuals = [(y_keyed[k] - y0_keyed[k]) for k in KEYS]
max_abs_residual = max ([abs (r) for r in residuals])

print ("==> A_keyed:", A_keyed)
print ("==> x_keyed:", x_keyed)
print ("==> True solution, y0_keyed:", y0_keyed)
print ("==> Your solution:", y_keyed)
print ("==> Residual (infinity norm):", max_abs_residual)
assert max_abs_residual <= 1e-14

print ("\n(Passed.)")
        
    
    
    
    
    
    