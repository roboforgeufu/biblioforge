class PriorityQueue {
    constructor() {
        this.queue = [];
    }

    put(item, priority) {
        this.queue.push({ item, priority });
        this.queue.sort((a, b) => a.priority - b.priority);
    }

    get() {
        if (this.queue.length === 0) throw new Error('Queue is empty');
        return this.queue.shift().item;
    }

    peek() {
        if (this.queue.length === 0) throw new Error('Queue is empty');
        return this.queue[0].item;
    }

    empty() {
        return this.queue.length === 0;
    }
}


function h_score(cell, destination) {
    origin_cell = matrix[cell[0]][cell[1]];
    destination_cell = matrix[destination[0]][destination[1]];

    cell_i = origin_cell.getAttribute('data-i');
    cell_j = origin_cell.getAttribute('data-j');
    destination_i = destination_cell.getAttribute('data-i');
    destination_j = destination_cell.getAttribute('data-j');

    return Math.abs(cell_i - destination_i) + Math.abs(cell_j - destination_j);
}

function findNeighbors(cell) {
    const neighbors = [];

    if (cell[0] > 0)
        matrix[cell[0] - 1][cell[1]].getAttribute('data-value') == 0 ? neighbors.push(matrix[cell[0] - 1][cell[1]]) : null;

    if (cell[0] < matrix.length - 1)
        matrix[cell[0] + 1][cell[1]].getAttribute('data-value') == 0 ? neighbors.push(matrix[cell[0] + 1][cell[1]]) : null;

    if (cell[1] > 0)
        matrix[cell[0]][cell[1] - 1].getAttribute('data-value') == 0 ? neighbors.push(matrix[cell[0]][cell[1] - 1]) : null;

    if (cell[1] < matrix.length - 1)
        matrix[cell[0]][cell[1] + 1].getAttribute('data-value') == 0 ? neighbors.push(matrix[cell[0]][cell[1] + 1]) : null;

    return neighbors;

}

function a_star() {
    destination = [0, 0];

    f_score = {};
    for (const i in matrix) {
        for (const j in matrix) {
            f_score[[i, j]] = Infinity;
        }
    }
    g_score = {};

    initial_cell = [matrix.length - 1, matrix[0].length - 1];
    g_score[initial_cell] = 0;
    f_score[initial_cell] = g_score[initial_cell] + h_score(initial_cell, destination);

    const queue = new PriorityQueue();
    queue.put(initial_cell, f_score[initial_cell])

    path = {}
    while (!queue.empty()) {
        new_cell = queue.get();

        matrix[new_cell[0]][new_cell[1]].style.backgroundColor = 'red';

        if (new_cell[0] == destination[0] && new_cell[1] == destination[1]) {
            break;
        }

        const neighbors = findNeighbors(new_cell);

        neighbors.forEach((element) => {
            const position = [parseInt(element.getAttribute('data-i')), parseInt(element.getAttribute('data-j'))];
            let new_g_score = g_score[new_cell] + 1;
            let new_f_score = new_g_score + h_score(position, destination);

            if (new_f_score < f_score[position]) {
                f_score[position] = new_f_score;
                g_score[position] = new_g_score;
                queue.put(position, new_f_score);
                path[position] = new_cell;
                matrix[position[0]][position[1]].style.backgroundColor = 'green';
            }
                        
            const p1 = document.createElement('p');
            const p2 = document.createElement('p');

            p1.classList.add('distance-text');
            p2.classList.add('distance-text');

            p1.innerText = g_score[position];
            p2.innerText = f_score[position] - g_score[position];

            element.innerHTML = '';

            element.appendChild(p1);
            element.appendChild(p2);
        })
    }

    if (destination in path) {
        let current_cell = destination;
        while (current_cell != initial_cell) {
            matrix[current_cell[0]][current_cell[1]].style.backgroundColor = 'purple';
            current_cell = path[current_cell];
        }
        matrix[initial_cell[0]][initial_cell[1]].style.backgroundColor = 'purple';
    }
}