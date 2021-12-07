const fs = require('fs')
const data = fs.readFileSync('inputs/day-3.txt').toString().split('\n')

// Part one
let gamma = ''
let epsilon = ''
for (i = 0; i < 12; i++) {
    let zeroes = 0
    let ones = 0

    data.forEach(n => {
        if (n[i] == '0') {
            zeroes++
        } else {
            ones++
        }
    })

    if (zeroes > ones) {
        gamma += '0'
        epsilon += '1'
    } else {
        gamma += '1'
        epsilon += '0'
    }
}
console.log(parseInt(gamma, 2) * parseInt(epsilon, 2))

// Part two
let o2 = data.map(x => x)
let co2 = data.map(x => x)

for (i = 0; i < 12; i++) {
    let zeroes = 0
    let ones = 0

    o2.forEach(n => {
        if (n[i] == '0') {
            zeroes++
        } else {
            ones++
        }
    })

    if (zeroes > ones) {
        for (j = o2.length - 1; j > -1; j--) {
            if (o2.length == 1) break

            if (o2[j][i] == '1') o2.splice(j, 1)
        }
    } else {
        for (j = o2.length - 1; j > -1; j--) {
            if (o2.length == 1) break

            if (o2[j][i] == '0') o2.splice(j, 1)
        }
    }

    if (o2.length == 1) break
}

for (i = 0; i < 12; i++) {
    let zeroes = 0
    let ones = 0

    co2.forEach(n => {
        if (n[i] == '0') {
            zeroes++
        } else {
            ones++
        }
    })

    if (zeroes > ones) {
        for (j = co2.length - 1; j > -1; j--) {
            if (co2.length == 1) break

            if (co2[j][i] == '0') co2.splice(j, 1)
        }
    } else {
        for (j = co2.length - 1; j > -1; j--) {
            if (co2.length == 1) break

            if (co2[j][i] == '1') co2.splice(j, 1)
        }      
    }

    if (co2.length == 1) break
}
console.log(parseInt(o2[0], 2) * parseInt(co2[0], 2))