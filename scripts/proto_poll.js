/*
In this code, the mergeObjects function is used to 
merge the properties of two objects. However, it is
vulnerable to prototype pollution because it does not 
properly check if the properties being merged are safe. 
If obj2 contains a property named __proto__, it can modify 
the prototype of obj1, potentially leading to unexpected 
behavior or security vulnerabilities.
*/

function mergeObjects(obj1, obj2) {
    for (var key in obj2) {
        if (obj2.hasOwnProperty(key)) {
            obj1[key] = obj2[key];
        }
    }
    return obj1;
}

var object1 = { a: 1, b: 2 };
var object2 = { b: 3, c: 4 };

var mergedObject = mergeObjects(object1, object2);
console.log(mergedObject);
