const products = [
    {name : 'cucumber', type: 'vegetable'},
    {name : 'banana', type: 'fruit'},
    {name : 'carrot', type: 'vegetable'},
    {name : 'apple', type: 'fruit'},
]

const vegeFilter = function (product) {
    return product.type === 'vegetable'
}
const vegetables = products.filter(vegeFilter)
console.log(vegetables)