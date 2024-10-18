#include "node.h"

Node::Node() {}

Node::Node(int index)
{
    _index = index;
}

int Node::getIndex()
{
    return _index;
}

void Node::addNeighbor(Edge *edge)
{
    neighbors.push_back(*edge);
    neighborsIndex[edge->destIndex] = neighbors.size() - 1;
}

Edge Node::getNeighbor(int neigIndex)
{
    return neighbors[neighborsIndex[neigIndex]];
}