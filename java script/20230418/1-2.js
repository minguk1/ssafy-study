words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    
    const ward = word.split('').reverse('').join('');
    if (word === ward) {
        return true
    }
    else { return false}
  }
  
for (const word of words) {
    
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false