const path = require('path');

module.exports = {
  entry: './src/aiuta-wrapper.js',
  output: {
    path: path.resolve(__dirname, 'docs/js'),
    filename: 'aiuta-try-on-sdk.js',
    clean: false,
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              ['@babel/preset-env', { targets: 'defaults' }],
              ['@babel/preset-react', { runtime: 'automatic' }]
            ]
          }
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.svg$/,
        type: 'asset/resource'
      }
    ]
  }
};