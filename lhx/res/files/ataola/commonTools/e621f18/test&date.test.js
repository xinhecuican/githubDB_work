const {date} = require('../index');

console.log(date.timestampDuration(Date.now()));
console.log(date.timestampDuration(86400000));
console.log(date.timestampDuration(3600000));
console.log(date.timestampDuration(60000));
console.log(date.timestampDuration(1000));


// console.log(date._toDateType(null));
// console.log(date._toDateType(undefined));
// console.log(date._toDateType('test it!'));
// console.log(date._toDateType('2020-05-06T11:52:29.048Z'));

// console.log(date.toString("Wed May 06 2020 20:19:30 GMT+0800 (中国标准时间)"));

console.log(date.dateFormat("Wed May 06 2020 20:19:30 GMT+0800 (中国标准时间)", 'YYYY-MM-DD'));
console.log(date.dateFormat("Wed May 06 2020 20:19:30 GMT+0800 (中国标准时间)", 'YYYY/MM/DD'));

