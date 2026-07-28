def solution(ineq, eq, n, m):
    if ineq == '<' and eq == '=': return int(n <= m)
    elif ineq == '<' and eq == '!': return int(n < m)
    elif ineq == '>' and eq == '=': return int(n >= m)
    elif ineq == '>' and eq == '!': return int(n > m)
    # operator = {
    #     "<=": n <= m,
    #     "<!": n < m,
    #     ">=": n >= m,
    #     ">!": n > m
    # }
    # return int(operator[ineq + eq])