from mathoperation .addOP import addvalue
from mathoperation .subop import subvalue

if __name__ == '__main__':
    print('this is main code')
    val1 = int(input('enter first number = '))
    val2 = int(input('enter second number = '))
    op = input('which math op you want to do ?  ')

    if op.lower()== 'add':
        # addition =(val1+val2)
        # print(f'addition = {addition}')
        a1 = addvalue(val1+val2)
        print(f'addition= {a1}')
    elif op.lower() == 'sub':
        # subtraction = (val1-val2)
        # print('subtraction',subtraction)
        a2 = subvalue(val1-val2)
        print('subtraction', a2)
    elif op.lower() ==''
    else:
        print('please choose correct operation, add ,sub')