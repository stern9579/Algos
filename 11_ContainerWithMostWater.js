function maxArea (height) {
    let max = 0;
    let p1 = 0;
    let p2 = height.length-1;
    
    while (p1 <= p2){
        
        if(height[p1]<height[p2]){
            let test = height[p1] * (p2-p1);
            if(test > max){
                max = test;
            }
            p1++;
        } else if (height[p1]>height[p2]){
            let test = height[p2] * (p2-p1);
            if(test > max){
                max = test;
            }
            p2--;
        } else {
            let test = height[p1] * (p2-p1);
            if(test > max){
                max = test;
            }
            if(height[p1+1]>height[p2-1]){
                p1++
            } else if(height[p1+1]<height[p2-1]){
                p2--
            } else{
                p1++;
                p2--;
            }
        }
    }
    return max;
}


console.log(maxArea([1,8,6,2,5,4,8,3,7]));