const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  function solution(K, N, M, chargers) {
    // console.log([K, N, M, chargers])
    let now = 0
    let cnt = 0
    // console.log([now,cnt])
    // console.log([now, cnt])
    while (now < N) {
        if (cnt === -1) {
            cnt = 0;
            break
        }
        let next = now + K
        if (next >= N) {
            break
        }
        for (t=next; t >= now; t--) {
            // console.log(t)
            if ( t === now ) {
                
                cnt = -1
                break
            }



            if ( chargers.includes(t)) {
                now = t
                cnt ++
                // console.log(t)
                break
            }



        }



    }
    return cnt


  }
  
  for (const input of inputs) {
    console.log(solution(input[0], input[1], input[2], input[3]))
  }