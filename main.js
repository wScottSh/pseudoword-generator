const cityList = require('./citylist');

const nameLengths = {}

const nameLengthFinder = (list) => {
  let lengthArray = []
  let maxLength, minLength

  for (let i = 0; i < list.length; i++) {
    lengthArray.push(list[i].length)
  }

  let spread = lengthArray.reduce( (acc, i) => {
    if (typeof acc[i] == 'undefined') {
      acc[i] = 1;
    } else {
      acc[i] += 1;
    }
    return acc;
  }, {});

  console.log(spread);
}

const lengthProbabilityMaker = (list) => {
  let lengths = nameLengthFinder(list)
  
}

lengthProbabilityMaker(cityList)
