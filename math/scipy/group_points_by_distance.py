from scipy.spatial.distance import cdist
from scipy.spatial.distance import pdist

def group_points_by_distance(coords, threshold):
    ''' Return group of points that are near that threshold. The points are
        identified by its index in the given array.

    :param coords: list of coordinate lists.
    :param threshold: upper limit of the distance to consider the points in the
                      same group.
    '''
    sz= len(coords)
    distances= cdist(coords, coords)
    groups= dict()
    already_grouped= set()
    for i in range(0,sz):
        if(i not in already_grouped):
            if(i not in groups):
                groups[i]= list()
                for j in range(i,sz):
                    if(j not in already_grouped):
                        d= distances[i][j]
                        if(d<threshold):
                            groups[i].append(j)
                            already_grouped.add(j)
    return groups


coords = [[1,2,3],[2,3,4],[3,4,5],[5,4,3],[3,4,5]]
for d in range(1, 6):
    groups= group_points_by_distance(coords, threshold= d)
    print(d, groups)
