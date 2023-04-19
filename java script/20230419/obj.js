const obj = {
    numbers : [1, 2],
    myfunc : function() {
        console.log(this)
        const in_my_func = function() {
            console.log(this)
        }
        in_my_func()
    }
}

obj.myfunc()

//화살표 함수

const obj2 = {
    numbers : [1, 2],
    myfunction() {
        console.log(this)
        const in_my_func = () => {
            console.log(this)
        }
        in_my_func()
    }
}

obj2.myfunction()