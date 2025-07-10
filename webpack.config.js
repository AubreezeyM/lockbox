const path = require('path');

module.exports = {
    entry: './react/index.js',
    output: {
        filename: 'react/index-bundle.js',
        path: path.resolve(__dirname, './static'),
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                }
            },
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx']
    }
};