#!/usr/bin/python3
'''UTF-8 Validation Program
'''


def validUTF8(data):
    '''Validate UTF8 characters list
    '''
    def CountLeft_Ones(lbyte):
        '''Count the number of first '1'
        '''
        count = 0
        for pos in range(7, -1, -1):
            if ((1 << pos) & lbyte):
                count += 1
            else:
                break
        return count

    if not isinstance(data, list) or type(data) is not list:
        return False
    if data == []:
        return True
    count = 0
    for d in data:
        if type(d) != int:
            return False
        if d > 255 or d < 0:
            return False
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
