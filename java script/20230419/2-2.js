const users = [
      { name: 'John', age: 31, isMarried: true, balance: 100, },
      { name: 'Sarah', age: 22, isMarried: false, balance: 200, },
      { name: 'Ashley', age: 25, isMarried: true, balance: 300, },
      { name: 'Robert', age: 27, isMarried: false, balance: 400, },
      { name: 'Tom', age: 35, isMarried: true, balance: 500, },
    ]

  users.forEach(function (user) {console.log(user['name'])})

  const married = users.filter(function (user) {return user['isMarried'] === true})
  console.log(married)

  const tom = users.find(function (user) {return user['name'] === 'Tom'})
  console.log(tom)

  const newUsers = users.map(function (user) {return {...user, isAlive : true}})
  console.log(newUsers)

  const totalBalance = users.reduce(function (total, user) {return total + user['balance']}, 0)
  console.log(totalBalance)