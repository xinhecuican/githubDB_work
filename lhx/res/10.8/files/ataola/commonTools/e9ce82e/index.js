const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

function randomLetters(length) {
	  let random;
	  let output = '';

	  for (let i = 1; i <= length; i++) {
		      output += letters.substring(random = Math.floor(Math.random() * letters.length), random + 1);
		    }
	  return output;
};

module.exports = randomLetters;
