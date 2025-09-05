#include <bits/stdc++.h>
#include "src/node.h"
#include "src/edge.h"
#include "src/graph.h"

using namespace std;
int main()
{

    Node a(0), b(1), c(2);

    Edge a_b(1, 10, 'N'), b_c(2, 9, 'S'), c_a(0, 12, 'O');
    a.addNeighbor(&a_b);
    b.addNeighbor(&b_c);
    c.addNeighbor(&c_a);

    Graph graph;
    graph.addNode(a);
    graph.addNode(b);
    graph.addNode(c);

    std::vector<Path> path;
    path = graph.dijkstra(0, 2);

    for (int i = 0; i < path.size(); i++)
    {
        cout << path[i].originIndex << " -> " << path[i].destinationIndex << " - " << path[i].distance << " - " << path[i].direction << '\n';
    }

    return 0;
}