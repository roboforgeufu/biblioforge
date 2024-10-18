#ifndef NODE_H
#define NODE_H

#include <vector>
#include <unordered_map>
#include <limits.h>
#include "edge.h"

class Node
{
public:
    int distanceToOrigin = INT_MAX;
    bool explored = false, blocked = false;
    Node *prev = nullptr;
    std::vector<Edge> neighbors;

    Node();

    Node(int index);

    int getIndex();

    void addNeighbor(Edge *edge);

    Edge getNeighbor(int neigIndex);

private:
    int _index;
    std::unordered_map<int, int> neighborsIndex;
};

#endif