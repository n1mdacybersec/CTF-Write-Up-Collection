const CryptoJS=require('crypto-js');

const key = '3d3067e197cf4d0a';
const ciphertext = 'U2FsdGVkX1+2k+cHVHn/CMkXGGDmb0DpmShxtTfwNnMr9dU1I6/GQI/iYWEexsod';

var bytes = CryptoJS.AES.decrypt(ciphertext, key);
var message = bytes.toString(CryptoJS.enc.Utf8);

console.log(message);
