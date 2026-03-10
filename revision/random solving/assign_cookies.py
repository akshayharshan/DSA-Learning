def assign_cookies(g,s):

    g.sort()
    s.sort()
    l,r =0,0
    counter = 0
    while l < len(g) and r < len(s):
        # cookie size should be greater than the greed of student as it is a sorted we have to move on the cookie pointer
        if s[r] >= g[l]:
            counter +=1
            l+=1
            r+=1
        else:
            r +=1
    return counter






if __name__ == "__main__":
    greed = [2, 3, 4]
    cookie = [1, 2, 3, 5]
    print(assign_cookies(greed,cookie))