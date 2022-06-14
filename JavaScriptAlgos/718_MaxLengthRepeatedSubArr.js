/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
function findLength(nums1, nums2) {
    let p1 = 0;
    let l = 0;

    while(p1< nums1.length){
        tempLength = 0;
        let p2 = 0
        while(p2 < nums2.length){
            if(nums2[p2] == nums1[p1]){
                tempLength ++;
                p1++;
            } 
            p2++;
        }
        if(tempLength > l){
            l = tempLength;
        }
    }
    return l;
};

console.log(findLength([1,2,3,2,1], [3,2,1,4,7]));
console.log(findLength([0,0,0,0,0], [0,0,0,0,0]));
console.log(findLength([0,0,0,0,1], [1,0,0,0,0]));

