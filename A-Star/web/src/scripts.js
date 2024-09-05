let size = localStorage.getItem('size');
let percent = localStorage.getItem('percent');
const grid = document.querySelector('.grid');
const inputSize = document.querySelector('#size');
const inputPercent = document.querySelector('#percent');
const generateButton = document.querySelector('.generate-button');
const distanceCheckbox = document.querySelector('.input-distance');
let matrix;
const maxPercent = 35;
const maxSize = 100;


if (!size) {
    size = 50;
    localStorage.setItem('size', size);
}
if (!percent) {
    percent = 10;
    localStorage.setItem('percent', percent);
}

inputSize.value = size;
inputPercent.value = percent;


function generateGrid(value) {
    grid.innerHTML = ''

    percent = inputPercent.value;
    localStorage.setItem('size', value);
    localStorage.setItem('percent', percent);

    matrix = [];

    for (let i = 0; i < value; i++) {
        matrix.push([]);
        for (let j = 0; j < value; j++) {
            const gridItem = document.createElement('div');
            gridItem.classList.add('grid-item');
            gridItem.setAttribute('data-i', i);
            gridItem.setAttribute('data-j', j);

            let wall = 0;

            if (i == 0 && j == 0) {
                gridItem.style.backgroundColor = 'lime';
            }
            else if (i == value - 1 && j == value - 1) {
                gridItem.style.backgroundColor = 'blue';
            }
            else {
                wall = Math.random() < (percent / 100) ? 1 : 0;
                gridItem.style.backgroundColor = wall ? 'white' : 'transparent';
            }

            gridItem.setAttribute('data-value', wall)

            grid.appendChild(gridItem);

            matrix[i].push(gridItem);
        }
    }

    grid.style.gridTemplateColumns = `repeat(${value}, 1fr)`;
}

document.body.onload = function () {
    generateGrid(size);
}

generateButton.addEventListener('click', () => generateGrid(inputSize.value));

inputPercent.addEventListener('input', () => {
    inputPercent.value > maxPercent ? inputPercent.value = maxPercent : null;
});

inputSize.addEventListener('input', () => {
    inputSize.value > maxSize ? inputSize.value = maxSize : null;
})

distanceCheckbox.addEventListener('change', () => {
    document.querySelectorAll('.distance-text').forEach((element) => {
        element.style.display = distanceCheckbox.checked ? 'block' : 'none';
    })
})