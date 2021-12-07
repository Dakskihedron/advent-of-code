const fs = require('fs')
const data = fs.readFileSync('inputs/day-1.txt').toString().split('\n')
console.log(data)

let count = 0

// Part one
for (let i = 1; i < data.length; i++) {
    if (Number(data[i]) > Number(data[i-1])) {
        count++
    }
}
console.log(count)

// Part two
count = 0
let prev = [Number(data[0]), Number(data[1]), Number(data[2])].reduce((x, y) => x + y, 0)
for (let i = 2; i < (data.length - 1); i++) {
    let now = [Number(data[i-1]), Number(data[i]), Number(data[i+1])].reduce((x, y) => x + y, 0)
    if (now > prev) {
        count++
    }
    prev = now
}
console.log(count)