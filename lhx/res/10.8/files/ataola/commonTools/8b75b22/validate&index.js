

class Validate {

  constructor() {
    this.regexp = {
      mobie: /^1[3|4|5|7|8][0-9]{9}$/,
      id_card: /^\d{17}(\d|x)$/i,
    }
  }

  isMobie(mobie) {
    const { regexp } =  this;
    if (regexp.mobie.test(mobie)) {
      return true;
    } else {
      return false;
    }
  }

  isIdCard(id_card) {
    const { regexp } = this;
    if (regexp.id_card.test(id_card)) {
      return true;
    } else {
      return false;
    }
  }

  static createValidate() {
    return new Validate();
  }
}

module.exports = Validate.createValidate();