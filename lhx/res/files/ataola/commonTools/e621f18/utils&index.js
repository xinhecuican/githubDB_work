class Util {

    sleep(millisecond) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve();
            }, millisecond);
        });
    }

    sleepNotRecommended(millisecond) {
        let start = Date.now();
        while (Date.now() - start < millisecond) {
            // donothing
            if (Date.now() - start >= millisecond) break;
        }
    }

    static createUtil() {
        return new Util();
    }
}

module.exports = Util.createUtil();