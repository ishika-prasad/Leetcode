
def heightChecker(heights):
    h2 = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != h2[i]:
            count += 1
    print(count)
    return count

if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    heightChecker(heights)