#include "graph.h"

Path::Path(int origIndex, int destIndex, int dist, char dir)
{
    distance = dist;
    originIndex = origIndex;
    destinationIndex = destIndex;
    direction = dir;
}

void Graph::addNode(Node vertex)
{
    nodes.push_back(vertex);
    nodeIndex[vertex.getIndex()] = nodes.size() - 1;
}

Node Graph::getSmallestNode()
{
    int minimun = INT_MAX;
    Node minNode;

    for (int i = 0; i < nodes.size(); i++)
    {
        if (nodes[i].explored || nodes[i].blocked)
            continue;
        if (nodes[i].distanceToOrigin <= minimun)
        {
            minimun = nodes[i].distanceToOrigin;
            minNode = nodes[i];
        }
    }

    return minNode;
}

void Graph::printNodes()
{
    for (int i = 0; i < nodes.size(); i++)
    {
        std::cout << nodes[i].getIndex() << " - " << nodes[i].distanceToOrigin << std::endl;
    }
}

std::vector<Path> Graph::dijkstra(int originIndex, int destIndex)
{
    setDistanceToMax();
    Node current;

    nodes[nodeIndex[originIndex]].distanceToOrigin = 0;
    current = nodes[nodeIndex[originIndex]];

    while (current.getIndex() != destIndex)
    {
        nodes[nodeIndex[current.getIndex()]].explored = true;

        for (int i = 0; i < current.neighbors.size(); i++)
        {
            int newDistance = current.distanceToOrigin + current.neighbors[i].distance;
            int neighborIndex = current.neighbors[i].destIndex;
            Node *neighbor = &nodes[nodeIndex[neighborIndex]];

            if (neighbor->distanceToOrigin > newDistance)
            {
                neighbor->distanceToOrigin = newDistance;
                neighbor->prev = &nodes[nodeIndex[current.getIndex()]];
            }
        }
        current = getSmallestNode();
    }

    std::vector<int> orderedIndex;
    Node currentPath = nodes[nodeIndex[destIndex]];
    while (currentPath.getIndex() != originIndex)
    {
        orderedIndex.push_back(currentPath.getIndex());
        currentPath = *currentPath.prev;
    }
    orderedIndex.push_back(currentPath.getIndex());

    std::vector<Path> path;
    for (int i = 0; i < orderedIndex.size() - 1; i++)
    {
        int currentIndex = orderedIndex[i];
        Node currentNode = nodes[nodeIndex[currentIndex]];
        Node previous = *currentNode.prev;
        Edge prevToCurrent = previous.getNeighbor(currentIndex);
        path.push_back(Path(previous.getIndex(), currentNode.getIndex(), prevToCurrent.distance, prevToCurrent.direction));
    }

    std::reverse(path.begin(), path.end());

    return path;
}

void Graph::setDistanceToMax()
{
    for (int i = 0; i < nodes.size(); i++)
    {
        nodes[i].distanceToOrigin = INT_MAX;
    }
}

void Graph::blockNode(int index) {
    nodes[nodeIndex[index]].blocked = true;
}

void Graph::unblockNode(int index) {
    nodes[nodeIndex[index]].blocked = false;
}