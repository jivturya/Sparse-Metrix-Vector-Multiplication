# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:44:28 2022

@author: patzo
"""

rows   = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6]
cols   = [1, 2, 4, 0, 2, 3, 0, 1, 3, 4, 1, 2, 5, 6, 0, 2, 5, 3, 4, 6, 3, 5]
values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def coo2csr(coo_rows, coo_cols, coo_vals):
    from operator import itemgetter
    C = sorted(zip(coo_rows, coo_cols, coo_vals), key=itemgetter(0))
    nnz = len(C)
    assert nnz >= 1

    csr_inds = [j for _, j, _ in C]
    csr_vals = [a_ij for _, _, a_ij in C]

    # Your task: Compute `csr_ptrs`
    row=max(coo_rows)+1
    csr_ptrs=[0]*(row+1)
    
    for i in range(nnz):
        csr_ptrs[coo_rows[i]+1]=csr_ptrs[coo_rows[i]+1]+1
    for i in range(row):
        csr_ptrs[i+1]=csr_ptrs[i+1]+csr_ptrs[i]
    return (csr_inds,csr_vals,csr_ptrs)

print(coo2csr(rows,cols,values))