// 3289. The Two Sneaky Numbers of Digitville
const getSneakyNumbers = (nums: number[]) => {
    return 'sh'
}

// For Displaying in HTML file ========== 
const getSneakyNumbers_2535 = () => {
    let nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
    const display = getSneakyNumbers(nums)


    const showResult: any = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
}

getSneakyNumbers_2535()