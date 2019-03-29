var path = require('path');

module.exports = {
    entry: './assets/dev/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'assets/dist')
    }
};