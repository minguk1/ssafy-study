// 1-1

const savedFile = {
    name: 'profile',
    extension: 'jpg',
    size: 29930
  }
    const {name, extension, size} = savedFile

  function fileSummary(file) {
      console.log(`The file ${file.name}.${file.extension} is size of ${file.size} bytes.`)
  }
  fileSummary(savedFile);

  // 1-2
  const data = {
    username: 'myName',
    password: 'myPassword',
    email: 'my@mail.com',
  }

  const {username, password, email} = data
  
  // 2
  function addNumbers(a,b, ...args) {
    const numbers = [a, b, ...args];
    return numbers.reduce((sum, number) => { 
      return sum + number
    }, 0)
  }

  console.log(addNumbers(1,2))

  // 3-1
  const defaultColors = ['red', 'green', 'blue'];
  const favoriteColors = ['navy', 'black', 'gold', 'white']
  const palette = [...defaultColors, ...favoriteColors]
  console.log(palette)

  // 3-2
  const info1 = { name: 'Tom', age: 30 }
  const info2 = { isMarried: true, balance: 3000 }
  const fullInfo = {...info1, ...info2}
  console.log(fullInfo)