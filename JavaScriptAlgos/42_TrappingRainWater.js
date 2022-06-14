function trap (height){
    let bottom;
    let rP;
    let lP;
    let p = 0
    let water = 0; 

    while (p < height.length){
        if(height[p]>height[p+1]){
            bottom = p+1;
            lP = p;
            p++;
        }
        if(height[p]< height[p+1]){
            p++;
            rP = p;

        }
    }
}
