let star = [' ',' ',' ',' ','*',' ',' ',' ',' ']
// console.log(star)

function stack(star) {
for (i = 1; i < 6; i++) {
    // console.log(star)
    console.log(star.join(''))
    star[4-i] = "*"
    star[4+i] = "*"
}

}
stack(star)