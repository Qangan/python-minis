def format_table(benchmarks, algos, results):
    mcl = max(len(case) for case in benchmarks)
    mtl = max(len(tp) for tp in algos)
    mrl = max(len(str(i)) for j in results for i in j)

    cell = max(mcl, mtl, mrl, 10)

    head = f"| {'Benchmark':<{cell}} | " + " | ".join(f"{tp:<{cell}}" for tp in algos) + " |"
    
    top =  "┏" + '-' * (len(head) - 2) + '┒'
    sep =  '|' + '-' * (len(head) - 2) + '|'
    bot = '┖' + '-' * (len(head) - 2) + '┛'
    
    print(top)
    print(head)
    print(sep)

    for case, rest in zip(benchmarks, results):
        row = f"| {case:<{cell}} | " + \
              ' | '.join(f"{val:<{cell}}" for val in rest) + " |"
        print(row)
    
    print(bot)

format_table(["best case", "worst case"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
format_table(["bc", "wc"], ["qs", "ms", "bs"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
