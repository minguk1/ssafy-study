console.log('Hi')


let connect = new Promise((resolve, reject) => {

    setTimeout(function () {
      console.log('SSAFY')
      resolve()
    }, 3000)

})

connect.then(() => {
    console.log('Bye')
})