// Problem Name
const funcName = (num : number[]) => {
    return num
}


let num : number[] = [5, 6, 6, 7,2]
const display = funcName(num)

// For Displaying in HTML file ========== 
// Don't have to edit this, change file name on index-ts.html
const showResult : any = document.querySelector(".app");
showResult.innerHTML = "This is result: " + display;