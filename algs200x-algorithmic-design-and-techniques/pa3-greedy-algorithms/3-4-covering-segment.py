#! python3
import sys
from collections import namedtuple


def optimal_points(segments):
    """ Calculate the points that minimize the number of visits for each overlap """

    # Sort segments in ascending order by right most point
    sorted_segments = sorted(segments, key=lambda x: x.end)

    # Loop and pop sorted segments until all segments have been covered
    points = []
    while sorted_segments:
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        # Loop over a copy of sorted_segments and remove points that fall in the overlap
        for sorted_segment in sorted_segments[:]:
            if sorted_segment.start <= point <= sorted_segment.end:
                sorted_segments.remove(sorted_segment)

    return points


if __name__ == '__main__':
    integers = sys.stdin.read()
    n, *data = map(int, integers.split())

    Segment = namedtuple('Segment', 'start end')
    s = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    p_list = optimal_points(s)
    print(len(p_list))
    for p in p_list:
        print(p, end=' ')
