'use strict';
const crypto = require('crypto');
const qr = require('qr-image');
const fs = require('fs');

module.exports = function(key) {
    this.key = key;
    return {
        encode: (str) => {
            let encoder = crypto.createCipher('aes-256-ctr', this.key);
            return encoder.update(str, 'utf8', 'hex');
        },
        decode: (str) => {
            let decoder = crypto.createDecipher('aes-256-ctr', this.key);
            return decoder.update(str, 'hex', 'utf8');
        },
        qrgen: (data, file) => {
            let dataToEncode = data || null;
            let outImage = file || null;
            if (dataToEncode !== null && outImage !== null) {
                qr.image(dataToEncode, {
                    type: 'png',
                    size: 20
                }).pipe(fs.createWriteStream(outImage));
                return true;
            } else {
                return false;
            }
        }
    }
}




// exports.hello = (user) => {
//     return "Hello Human " + user;
// }

// The module.exports implementation
// NB: With this new implementation, you can't just use require alone in the other app:
// You use require, and then instantiate an object, since it's returning a Constructor

