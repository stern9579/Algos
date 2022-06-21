def RunnerUp(input):

    arr = map(int, input.split())
    
    a = list(arr)
    a.pop(0)
    
    runner_up = first = a[0]
    for i in a[1:]:
        if i > first:
            runner_up, first = first, i
            continue

        if runner_up < i < first:
            runner_up = i
        elif i < runner_up == first:
            runner_up = i

    print(runner_up)



RunnerUp("5 4 5 1 3 7")
RunnerUp("9 2 3 10 11 10 13")
RunnerUp("2 3 1 1 1 1")
RunnerUp("4 1 -1 -2 -1")
