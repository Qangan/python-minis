def format_table(benchmarks, algos, results):
    mcl = max(len(case) for case in benchmarks)
    mtl = max(len(tp) for tp in algos)
    
    head = f"| {'Benchmark':<{mcl}} | " + " | ".join(f"{tp:<{mcl}}" for tp in algos) + " |"
    
    top =  "┏" + '-' * (len(head) - 2) + '┒'
    sep =  '|' + '-' * (len(head) - 2) + '|'
    bot = '┖' + '-' * (len(head) - 2) + '┛'
    
    print(top)
    print(head)
    print(sep)

    for case, rest in zip(benchmarks, results):
        row = f"| {case:<{mcl}} | " + \
              '| '.join(f"{val:<{mtl}}" for val in rest) + " |"
        print(row)
    
    print(bot)

format_table(["best case", "worst case"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
