// http://erlycoder.com/105/javascript-weighted-random-value-from-array

var fruits=['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
var fruitweight=[5, 48, 117, 259, 304, 274, 280, 263, 171, 122, 75, 33, 20, 22, 8, 2, 3, 2, 3] //weight of each element above
// var fruits=["Apples", "Oranges", "Grapes", "Bananas"]
// var fruitweight=[2, 3, 1, 4] //weight of each element above
var fruitweight_norm = new Array() //normalized weights
var currentfruit=0

var sum = 0;
for (i=0; i<fruits.length; i++){
    sum += fruitweight[i];
    fruitweight_norm[i] = sum;
}
// console.log(fruitweight_norm);

for (i=0; i<fruits.length; i++){
    fruitweight_norm[i] = fruitweight_norm[i]/sum;
}
// console.log(fruitweight_norm);

function get_rand(){
    var rand = Math.random();
    var prev = 0;
    for (i=0; i<fruits.length; i++){
        console.log("Random range - "+prev+" : "+fruitweight_norm[i]);
        // document.write("Random range - "+prev+" : "+fruitweight_norm[i]+"<br>");
        if((prev<rand)&&(fruitweight_norm[i]>rand)){
          console.log(i);
            return i;
        }
        prev = fruitweight_norm[i];
    }
}

function get_fast(){
    needle = Math.random();
    high = fruitweight_norm.length - 1;
    low = 0;

    while(low < high){
        probe = Math.ceil((high+low)/2);

        if(fruitweight_norm[probe] < needle){
            low = probe + 1;
        }else if(fruitweight_norm[probe] > needle){
            high = probe - 1;
        }else{
            return probe;
        }
    }

    if(low != high ){
        return (fruitweight_norm[low] >= needle) ? low : probe;
    }else{
        return (fruitweight_norm[low] >= needle) ? low : low + 1;
    }
}

tmp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
// tmp = [0,0,0,0];

for (var i = 0; i < 100; i++) {
  console.log((get_fast() + 3) + ', ');
}

// for (i=0; i<100; i++){
//     id = get_fast();
//     tmp[id] += 1;
// }
//
// // for (i=0; i<4; i++){
// for (i=0; i<fruits.length; i++){
//   console.log("Randoms - "+ (i + 3) +" = "+tmp[i]);
//     // document.write("Randoms - "+i+" = "+tmp[i]+"<br>");
// }
