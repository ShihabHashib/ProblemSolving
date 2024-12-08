// 1588. Sum of All Odd Length Subarrays
const sumOddLengthSubarrays = (arr: number[]) => {
    let len: number = arr.length
    let total: number = 0;

    for (let i = 0; i < len; i++) {
        total += arr[i] * (
            Math.floor((i + 1) / 2) * Math.floor((len - i) / 2) +
            Math.ceil((i + 1) / 2) * Math.ceil((len - i) / 2)
        );
    }
    return total;

}


// For Displaying in HTML file ========== 
const sumOddLengthSubarrays_2535 = () => {
    let arr = [1, 4, 2, 5, 3]
    const display = sumOddLengthSubarrays(arr)


    const showResult: any = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
}

sumOddLengthSubarrays_2535()