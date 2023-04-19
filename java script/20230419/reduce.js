var fruits = ['apple', 'orange', 'apple', 'melon', 'orange', 'orange']

const f_count = fruits.reduce((counts, fruit) => {
    if (fruit in counts) {counts[fruit]++}
    else {counts[fruit] = 1}
    return counts
}, {})

console.log(f_count)