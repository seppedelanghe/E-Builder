import math

def quadratic(p0, p1, p2, t):
    return {
        'x': (math.pow(1 - t, 2) * p0.x + (1 - t) * 2 * t * p1.x + t * t * p2.x),
        'y': (math.pow(1 - t, 2) * p0.y + (1 - t) * 2 * t * p1.y + t * t * p2.y)
    }

def quadraticControlPoint(p0, p1, p2):
    return {
        'x': (p1.x * 2 - (p0.x + p2.x) / 2),
        'y': (p1.y * 2 - (p0.y + p2.y) / 2)
    }

def cubic(p0, p1, p2, p3, t):
    return {
        'x': (math.pow(1 - t, 3) * p0.x + math.pow(1 - t, 2) * 3 * t * p1.x + (1 - t) * 3 * t * t * p2.x + t * t * t * p3.x),
        'y': (math.pow(1 - t, 3) * p0.y + math.pow(1 - t, 2) * 3 * t * p1.y + (1 - t) * 3 * t * t * p2.y + t * t * t * p3.y)
    }


def multicurce(points):
    moves = []

    i = 0

    while i < len(points) - 2:
        p0 = points[i]
        p1 = {
            "x": (p0.x + points[i+1].x) / 2,
            "y": (p0.y + points[i+1].y) / 2
        }
        p2 = {
            "x": (p1['x'] + points[i+2].x) / 2,
            "y": (p1['x'] + points[i+2].y) / 2
        }

        moves.append(quadratic(p0, p1, p2, 1))

        i += 2
    
    p0 = points[i]
    p1 = {
        "x": (p0.x + points[i+1].x) / 2,
        "y": (p0.y + points[i+1].y) / 2
    }
    end = points[-1]

    moves.append(quadratic(p0, p1, end, 1))

    return moves
