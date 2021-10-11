class ZjtDate {
    _toDateType(date) {
        if ([undefined, null].some(value => value === date)) {
            throw new Error(`${date} is not a Date Type`);
        }

        if (typeof date === 'string') {
            const newDate = new Date(date);
            if (!isNaN(newDate)) {
                return newDate;
            } else {
                throw new Error(`${date} is not a Date Type`);
            }
        }

        return date;
    }

    timestampDuration(timestamp) {
        const minute = 60;
        const hour = 60 * minute;
        const day = 24 * hour;
        let str = '';
        timestamp = Math.round(timestamp / 1000);

        while (timestamp !== 0) {
            if (timestamp >= day) {
                str += `${Math.floor(timestamp / day)}天`;
                timestamp = timestamp % day;
            } else if (timestamp >= hour) {
                str += `${Math.floor(timestamp / hour)}小时`;
                timestamp = timestamp % hour;
            } else if (timestamp >= minute) {
                str += `${Math.floor(timestamp / minute)}分钟`;
                timestamp = timestamp % minute;
            } else {
                str += `${timestamp}秒`
                timestamp = 0;
            }
        }
        return str;
    }

    toString(date) {
        const newDate = this._toDateType(date);
        const year = newDate.getFullYear();
        const month = ('0' + (newDate.getMonth() + 1)).slice(-2);
        const day = ('0' + newDate.getDate()).slice(-2);
        const hour = ('0' + newDate.getHours()).slice(-2);
        const minute = ('0' + newDate.getMinutes()).slice(-2);
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const yesterday = new Date(today.getTime() - 24 * 60 * 60 * 1000);
        const dayBeforeYesterday = new Date(today.getTime() - 48 * 60 * 60 * 1000);
        const time = Math.round((Date.now() - newDate) / 1000);
        if (time < 30) return '刚刚';
        if (time < 60) return `${time}秒前`;
        if (time < 60 * 60) return `${Math.floor(time / 60)}分钟前`;
        if (time < 24 * 60 * 60) return `${Math.floor(time / (60 * 60))}小时前`;
        if (newDate < dayBeforeYesterday) return `${year}-${month}-${day} ${hour}:${minute}`;
        if (newDate < yesterday) return `前天 ${hour}:${minute}`;
        if (newDate < today) return `昨天 ${hour}:${minute}`;
        return '未知时间格式';
    }

    dateFormat(date, type) {
        const newDate = this._toDateType(date);
        const year = newDate.getFullYear();
        const month = (newDate.getMonth() + 1) < 10 ? '0' + (newDate.getMonth() + 1) : (newDate.getMonth() + 1);
        const day = newDate.getDate() - 1 < 10 ? '0' + newDate.getDate() : newDate.getDate();
        const hour = newDate.getHours() < 10 ? '0' + newDate.getHours() : newDate.getHours();
        const minute = newDate.getMinutes() < 10 ? '0' + newDate.getMinutes() : newDate.getMinutes();
        const second = newDate.getSeconds() < 10 ? '0' + newDate.getSeconds() : newDate.getSeconds();
        if (type === 'YYYY-MM-DD HH:MM:SS') {
            return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
        } else if (type === 'YYYY/MM/DD HH:MM:SS') {
            return `${year}/${month}/${day} ${hour}:${minute}:${second}`;
        } else if (type === 'YYYY-MM-DD') {
            return `${year}-${month}-${day}`;
        } else if (type === 'YYYY/MM/DD') {
            return `${year}/${month}/${day}`;
        } else {
            return '未知时间格式';
        }
    }

    static createDate() {
        return new ZjtDate();
    }
}

module.exports = ZjtDate.createDate();