/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
function findLength(nums1, nums2) {
    var dict = {};
    var dict2 = {};
    var length;


    if(nums1.length >= nums2.length){
        length = nums1.length
    } else {
        length = nums2.length
    }

    for(let x = 0; x <length; x++){
        if(dict[nums1[x]]){
            dict[nums1[x]] += 1;
        } else if(!dict[nums1[x]]){
            dict[nums1[x]] = 1;
        }
        if(dict2[nums2[x]]){
            dict2[nums2[x]] += 1;
        } else if(!dict2[nums2[x]]){
            dict2[nums2[x]] = 1;
        }
    }

    for(key in dict){
        if(dict2[key]){
            if(dict2[key] < dict[key]){
                length += dict2[key];
            } else {
                length += dict[key];
            }
        }
    }
    return length;
};

console.log(findLength([1,2,3,2,1], [3,2,1,4,7]));
console.log(findLength([0,0,0,0,0], [0,0,0,0,0]));