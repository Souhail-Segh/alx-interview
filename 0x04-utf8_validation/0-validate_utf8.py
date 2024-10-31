#!/usr/bin/env python3
from typing import List
'''UTF-8 Validation Program
'''


def validUTF8(data: List) -> bool:
    '''Validate UTF8 characters list
    '''
    def CountLeft_Ones(lbyte: int) -> int:
        '''Count the number of first '1'
        '''
        count = 0
        for pos in range(7, -1, -1):
            if ((1 << pos) & lbyte):
                count += 1
            else:
                break
        return count

    count = 0
    for d in data:
        if not count:
            count = CountLeft_Ones(d)
            if count == 0:
                continue
            if count > 4 or count == 1:
                return False
            count -= 1
        else:
            if CountLeft_Ones(d) != 1:
                return False
            count -= 1

    if count == 0:
        return True
    else:
        return False
