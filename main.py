from mathoperation.multiop import multivalue
from mathoperation.divop import divide

if __name__=='__main__':
    val1 = int(input('enter first value: '))
    val2 = int(input('enter second value: '))
    op = input('which math op you want to perform ?  ')

    if op.lower() =='multi':
        A1 = multivalue(val1,val2)
        print(f'multiplication: {A1}')
    elif op.lower() =='div':
        A2 = divide(val1,val2)
        print(f'division: {A2}')
    else:
        print('please choose the operation you want perform multi, div')