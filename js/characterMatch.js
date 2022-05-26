exports.isCharacterMatch = function(string1, string2) {

    string1 = string1.toLowerCase().replaceAll(" ", "").split("");
    string2 = string2.toLowerCase().replaceAll(" ", "").split("");

    if (!(string1.length === string2.length)) {
        return false;
    }

    for (let i=0; i<string1.length; i++) {
        if (string2.includes(string1[i])) {
            string2 = string2.join("").replace(string1[i],"");
            string2 = string2.split("")
        }
        }
    return (string2.length == 0) ? true : false;
};
