function myfunc(n) {
    console.log(n)
}

myfunc(4)

const myfunc2 = function(n) {
    console.log(n)
}
myfunc2(5)

const myfunc3 = function factioial(n) {
    console.log(n)
    if (n<=1) {
        return 1
    }
    return n * factioial(n-1)
}

console.log(myfunc3(3))