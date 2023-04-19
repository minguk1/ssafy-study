class Member {
    constructor(name, age) {
        this.name = name
        this.age = age
    }
    introduce() {
        console.log(`My name is ${this.name}`)
    }
}

const me = new Member("김태형", "24")

console.log(me.name)

me.introduce()

