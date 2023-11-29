// 2161. Partition Array According to Given Pivot
const pivotArray = (nums: number[], pivot: number) => {
    let left: number[] = []
    let right: number[] = []
    let center: number[] = []
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] < pivot) left.push(nums[i])
        else if (nums[i] > pivot) right.push(nums[i])
        else center.push(nums[i])
    }
    return [...left, ...center, ...right]
}

// For Displaying in HTML file ========== 
const displayResult_2161 = () => {
    let nums = [9, 12, 5, 10, 14, 3, 10]
    let pivot = 10
    const display = pivotArray(nums, pivot)


    const showResult: any = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
}

displayResult_2161()