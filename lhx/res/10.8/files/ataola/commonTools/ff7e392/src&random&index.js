const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
const NUMBERS = '0123456789'
const _generateRandom = Symbol('_generateRandom')

class Random {

  _generateRandom(raw, length) {
    let random = null;
    let output = '';
    for (let i = 0; i <= length; i++) {
      output += raw.substring(random = Math.floor(Math.random() * raw.length), random + 1);
    }
    return output;
  }

  letters(length) {
    return this._generateRandom(LETTERS, length);
  }

  numbers(length) {
    return this._generateRandom(NUMBERS, length);
  }

  static createRandom() {
    return new Random();
  }

}

module.exports = Random.createRandom();