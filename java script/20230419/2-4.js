class Monster {
    constructor(options) {
        this.health = 100
        this.name = options.name

    }
}

class Snake extends Monster {
    constructor(options) {
        super(options)
    }

    bite(snake) {
        snake.health -= 10
    }
}

const conda = new Snake({ name : 'conda'})
const boa = new Snake({ name : 'boa' })

console.log(conda.health)
boa.bite(conda)
console.log(conda.health)