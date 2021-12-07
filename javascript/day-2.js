const fs = require('fs')
const data = fs.readFileSync('inputs/day-2.txt').toString().split('\n')
for (i = 0; i < data.length; i++) {
    data[i] = data[i].split(/ +/g)
}

let hPos = 0
let depth = 0
let aim = 0

// Part one
data.forEach(step => {
    if (step[0] == 'forward') {
        hPos += Number(step[1])
    } else if (step[0] == 'down') {
        depth += Number(step[1])
    } else {
        depth -= Number(step[1])
    }
})
console.log(hPos * depth)

// Part two
hPos = 0
depth = 0
data.forEach(step => {
    if (step[0] == 'forward') {
        hPos += Number(step[1])
        depth += aim * Number(step[1])
    } else if (step[0] == 'down') {
        aim += Number(step[1])
    } else {
        aim -= Number(step[1])
    }
})
console.log(hPos * depth)