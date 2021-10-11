const {utils} = require('../index');

// test 1
// (async function() {
//     console.log('action biu!')
//     await utils.sleep(3000);
//     console.log('after sleep 3 second!');
// })();

// test 2
// (async () => {
//     console.log('action biu!');
//     utils.sleep(3000);
//     console.log('not after sleep 3 second!');
// })();

// test 3

(() => {
    console.log('action biu!');
    utils.sleepNotRecommended(3000);
    console.log('after sleep 3 second!');
})()