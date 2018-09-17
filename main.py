import matplotlib.pyplot as plt
import csv
import sys
import time
from point import Point


def plot(p):
    plt.plot(p.x, p.y, "o")


def plot_hull(hull):
    start = hull[0]
    for i in range(1, len(hull)+1):
        # if target reaches last point, make the target to initial point
        if i == len(hull):
            target = hull[0]
        else:
            target = hull[i]
        lines = plt.plot([start.x, target.x], [start.y, target.y])
        plt.setp(lines, linewidth=2, color="b")
        start = target


def cross_product(p1, p2, p3):
    dy1 = p2.y - p1.y
    dx1 = p2.x - p1.x
    dy2 = p3.y - p2.y
    dx2 = p3.x - p2.x
    return dy1 * dx2 - dx1 * dy2  # returning cross product of 3 points


def distance(p1, p2, p3):
    dy1 = p2.y - p1.y
    dx1 = p2.x - p1.x
    dy2 = p3.y - p2.y
    dx2 = p3.x - p2.x
    distance1 = (dy1 ** 2 + dx1 ** 2) ** 0.5
    distance2 = (dy2 ** 2 + dx2 ** 2) ** 0.5
    if distance1 == distance2:
        return 0
    elif distance1 > distance2:
        return 1
    else:
        return -1


def find_left_most(points):
    temp_min = points[0]
    for i in range(1, len(points)):
        if temp_min.x > points[i].x:
            temp_min = points[i]
    return temp_min


def hull(start_point, points):
    curr_point = start_point
    hull = []
    collinear_points = []
    hull.append(start_point)

    while True:
        next_point = points[0]
        for i in range(1, len(points)):
            if curr_point == points[i]:
                continue
            cp = cross_product(curr_point, next_point, points[i])
            # points[i] is on left of curr_point
            if cp > 0:
                next_point = points[i]  # move points[i] to next_point
                collinear_points = []   # empty the collinear_points list
            # points[i] is a collinear with curr_point
            elif cp == 0:
                # checking which point from next_point or points[i] is closer to our curr_point
                if distance(curr_point, next_point, points[i]) < 0:
                    # next point is closer to current point hence add to collinear list
                    collinear_points.append(next_point)
                    next_point = points[i]
                else:
                    collinear_points.append(points[i])

        # add all collinear points to hull list
        for point in collinear_points:
            hull.append(point)

        # if we have successfully iterated through all points then exit loop
        if next_point == start_point:
            break

        curr_point = next_point
        hull.append(curr_point)
        print(len(hull))
    return hull


file_name = str(sys.argv[1])  # reading second parameter from bash run
points = []
# reading csv file by header x, y
with open(file_name, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # initiating point objects
        p = Point(float(row['x']), float(row['y']))
        plot(p)
        points.append(p)

current_point = find_left_most(points)
start = time.time()
hull = hull(current_point, points)
end = time.time()
print(end - start)
plot_hull(hull)
plt.show()
