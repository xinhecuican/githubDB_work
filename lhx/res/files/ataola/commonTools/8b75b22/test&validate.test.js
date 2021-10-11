const {
  validate
} = require('../index');

const mobie_arr = [13732511234, 15715860123, 13858174566, 14457494011, 17877886655, 18788774455];
for (const mobie of mobie_arr) {
  const res = validate.isMobie(mobie) ? 'is validate' : 'is not validate';
  console.log(`${mobie} ${res}`);
}


const id_card_arr = ['33082119971221567x', 440824199706176677];
for (const id_card of id_card_arr) {
  const res = validate.isIdCard(id_card) ? 'is validate' : 'is not validate';
  console.log(`${id_card} ${res}`)
}