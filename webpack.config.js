const path = require('path');

module.exports = {
    entry: {
        markdown: {
            import: './blog/react/PostView.tsx',
            dependOn: 'react',
        },
        react: ['react', 'react-dom'],
    },
    output: {
        filename: 'react/[name]-bundle.js',
        path: path.resolve(__dirname, './static'),
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx|ts|tsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                }
            },
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.ts', '.tsx']
    },
};