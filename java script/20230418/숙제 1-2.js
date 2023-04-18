// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
    console.log('nums[' + i + ']: ' + nums[i])
  console.log(`nums[${ i }]: ${ nums[i] }`)
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.
// const로 선언한 변수는 재할당이 불가능하므로 let 으로 선언해준다.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}

// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
// for 안 in을 쓴다면 속성 이름을 통해 반복하고,
// of 을 쓴다면 속성 값을 통해 반복한다. 따라서 of를 이용하여 반복해준다.