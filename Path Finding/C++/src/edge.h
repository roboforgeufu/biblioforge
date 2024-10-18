#ifndef EDGE_H
#define EDGE_H

class Edge
{
public:
    int destIndex, distance;
    char direction;

    Edge(int dest, int dist, char dir);
};

#endif