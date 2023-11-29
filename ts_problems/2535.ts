// 2535. Difference Between Element Sum and Digit Sum of an Array
const differenceOfSum = (nums: number[]) => {
    const sumOfArr: number = nums.reduce((a, b) => a + b, 0)
    const sumOfDigits: number = nums.reduce((sum, num) => {
        const digits = num.toString().split('').map(Number);
        return sum + digits.reduce((digitSum, digit) => digitSum + digit, 0);
    }, 0);

    return sumOfArr - sumOfDigits
}

// For Displaying in HTML file ========== 
const displayResult_2535 = () => {
    let nums = [1, 15, 6, 3]
    const display = differenceOfSum(nums)


    const showResult: any = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
}

displayResult_2535()