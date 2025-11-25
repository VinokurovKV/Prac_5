class Base:
    a, b, c = input().split()

while s := input():
    match s.split():
        case [Base.a, *words] if 'yes' in words:
            print('case 1')
        case [Base.b]:
            print('case 2')
        case [Base.c, *words, Base.b]:
            print('case 3')

