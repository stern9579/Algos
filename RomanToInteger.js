/**
 * @param {string} s
 * @return {number}
 */

var string = "abc"
console.log(string.charAt(0))

function romanToInt(s) {
    var number = 0;
    for(var x = s.length-1; x >=0 ; x--){
        if(s.charAt(x)== "I"){
            number += 1;
        }
        if(s.charAt(x)== "V"){
            if (s.charAt(x-1)== "I"){
                number += 4;
                x--;
            } else {
                number += 5;
            }
        }
        if(s.charAt(x) == "X"){
            if (s.charAt(x-1)== "I"){
                number += 9;
                x--;
            } else {
                number += 10;
            }
        }
        if(s.charAt(x) == "L"){
            if (s.charAt(x-1)== "X"){
                number += 40;
                x--;
            } else {
                number += 50;
            }
        }
        if(s.charAt(x) == "C"){
            if (s.charAt(x-1)== "X"){
                number += 90;
                x--;
            } else {
                number += 100;
            }
        }
        if(s.charAt(x) == "D"){
            if (s.charAt(x-1)== "C"){
                number += 400;
                x--;
            } else {
                number += 500;
            }
        }
        if(s.charAt(x) == "M"){
            if (s.charAt(x-1)== "C"){
                number += 900;
                x--;
            } else {
                number += 1000;
            }
        }
    }
    return number;
}

console.log(romanToInt("III"));
console.log(romanToInt("VIII"));
console.log(romanToInt("IV"));
console.log(romanToInt("XIV"));
console.log(romanToInt("XIX"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));


