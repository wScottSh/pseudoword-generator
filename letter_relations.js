const cityList = require('./citylist');

const cities = cityList.join(' ').toLowerCase()
const alphabet = 'abcdefghijklmnopqrstuvwxyz -'.split('');
let occurances = {}

for (var i = 0; i < alphabet.length; i++) {
  let regex = new RegExp(alphabet[i] + '', 'g');
  let num = cities.match(regex).length
  occurances[alphabet[i]] = num
}

module.exports = occurances
