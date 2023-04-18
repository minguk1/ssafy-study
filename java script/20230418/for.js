const arr = [3, 5, 7]

for (const i in arr) {
    console.log(i)
}

for (const i of arr) {
    console.log(i)
}

console.log('*'+'*')
let x = 5

for (let i = 1; i < 6; i++) {
    let star = ""
    for (let j = 1; j <= i; j++) {
        star += "*"
    }
    console.log(star)
}