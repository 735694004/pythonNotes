function merge(left,right){
    let i=0,j=0
    let res = []
    while(i<left.length&&j<right.length){
        if(left[i]<right[j]){
            res.push(left[i])
            i++
        }else{
            res.push(right[j])
            j++
        }
    }
    res=res.concat(left.splice(i))
    res=res.concat(right.splice(j))
    return res
}
function mergeSort(arr){
    if(arr.length<=1){
        return arr
    }
    let mid = parseInt(arr.length/2)
    let left = arr.splice(0,mid)
    let right =arr
    return merge(mergeSort(left),mergeSort(right))
}
let li =  [17, 33, 17, 59, 19, 14, 33, 15, 16, 19, 4]
console.log(mergeSort(li))