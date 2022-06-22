if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum = 0.00
    for score in student_marks[query_name]:
        sum = float(sum) + score
        
    avg = sum/3
    
    
    format_avg = "{:.2f}".format(avg)
        
    print(format_avg)
        