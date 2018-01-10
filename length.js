const cityList = require('./citylist');

let nameLengths = {}
let nameRatios = {}

const nameLengthFinder = (list) => {
  let lengthArray = []
  let maxLength, minLength

  for (let i = 0; i < list.length; i++) {
    lengthArray.push(list[i].length)
  }

  let occuranceObj = lengthArray.reduce( (acc, i) => {
    if (typeof acc[i] == 'undefined') {
      acc[i] = 1;
    } else {
      acc[i] += 1;
    }
    return acc;
  }, {});

  nameLengths = occuranceObj;
}

let ratioMaker = (obj) => {
  // let l = Object.keys(nameLengths).length
  let valueArray = Object.values(obj)
  let maxNum = Math.max(...valueArray)
  // console.log(maxNum);

  let ratio = (num1, num2) => {
    return num1 / num2
  }

  Object.keys(obj).forEach(function(key) {
    // console.log(obj[key]);
    nameRatios[key] = ratio(obj[key], maxNum)
  })
}

const lengthProbabilityMaker = (list) => {
  nameLengthFinder(list)
  ratioMaker(nameLengths)
  console.log(nameRatios);
}

lengthProbabilityMaker(cityList)

module.exports = nameRatios
