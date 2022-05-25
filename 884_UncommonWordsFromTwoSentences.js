/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[]}
 */
function uncommonFromSentences(s1, s2) {
    var word = ""
    var dict = {};
    var uniqueWords = [];

    for (var x = 0; x < s1.length; x++) {
        if (s1.charAt(x) != " ") {
            word += s1.charAt(x);
        } else {
            if (dict[word]) {
                dict[word] += 1;
                word = "";
            } else {
                dict[word] = 1;
                word = "";
            }
        }
    }
    if (dict[word]) {
        dict[word] += 1;
        word = "";
    } else {
        dict[word] = 1;
        word = "";
    }

    for (var x = 0; x < s2.length; x++) {
        if (s2.charAt(x) != " ") {
            word += s2.charAt(x);
        } else {
            if (dict[word]) {
                dict[word] += 1;
                word = "";
            } else {
                dict[word] = 1;
                word = "";
            }
        }
    }
    if (dict[word]) {
        dict[word] += 1;
        word = "";
    } else {
        dict[word] = 1;
        word = "";
    }

    for (key in dict) {
        if (dict[key] == 1) {
            uniqueWords.push(key)
        }
    }

    return word, dict, uniqueWords;
};

console.log(uncommonFromSentences("this apple is sweet", "this apple is sour"))

let str = "this apple is sweet"

console.log(str.split(" "));