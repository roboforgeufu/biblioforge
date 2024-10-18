#ifndef GRAPH_H
#define GRAPH_H

#include <vector>
#include <unordered_map>
#include <limits.h>
#include <iostream>
#include <algorithm>
#include "node.h"

class Path
{
public:
    int distance, originIndex, destinationIndex;
    char direction;

    Path(int origIndex, int destIndex, int dist, char dir);
};

class Graph
{
public:
    void addNode(Node vertex);

    Node getSmallestNode();

    void printNodes();

    std::vector<Path> dijkstra(int originIndex, int destIndex);

private:
    std::unordered_map<int, int> nodeIndex;
    std::vector<Node> nodes;

    void setDistanceToMax();
};

#endif