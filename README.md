# Andrew's Monotone Chain Convex Hull Algorithm

Computes the Convex Hull of a Set of 2D Points

## Convex Hull Function

The algorithm comes from [this page](https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python).

```Python
convex_hull(points)
```

* Input : an iterable sequence of ```(x, y)``` pairs representing the points.

* Output : a list of vertices of the convex hull in counter-clockwise order,
starting from the vertex with the lexicographically smallest coordinates.
Andrew's monotone chain algorithm has a ```O(n log(n))``` complexity.

## Convex Hull Visualisation

Output example with ```50``` vertices :

![convex hull example](convex-hull-example.png)
