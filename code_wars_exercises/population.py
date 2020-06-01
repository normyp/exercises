def nb_year(p0, percent, aug, p):
    # your code
    # return n number of years needed to get population greater than or equal to p
    n = 0
    percent = percent/100
    while p0 < p:
        p0 = p0 + p0 * percent + aug
        n += 1
    print(n)

nb_year(1500, 5, 100, 5000)
