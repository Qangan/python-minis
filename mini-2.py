print((lambda x, y: ([(x[i], y[i]) for i in range(min(len(x), len(y)))]))(eval('[' + ', '.join(input().split()) + ']'), eval('[' + ', '.join(input().split()) + ']')))
