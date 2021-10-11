const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production';
  return {
    mode: isProduction ? 'production' : 'development',
    entry: path.resolve(__dirname, 'src/index.js'),
    output: {
      publicPath: '',
      filename: 'paramita.min.js',
      path: path.resolve(__dirname, 'dist'),
    },
    devtool: 'source-map',
    resolve: {
      extensions: ['.css', '.scss'],
      alias: {
        // Provides ability to include node_modules with ~
        '~': path.resolve(process.cwd(), 'src'),
      },
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: [{ loader: 'babel-loader' }]
        },
        {
          test: /\.s[ac]ss$/i,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
            {
              loader: 'css-loader',
              options: {
                sourceMap: isProduction,
              },
            },
            {
              loader: 'postcss-loader',
              options: {
                postcssOptions: {
                  plugins: ['postcss-preset-env', 'autoprefixer', 'cssnano']
                }
              }
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: isProduction,
                implementation: require('sass'),
                sassOptions: {
                  fiber: false,
                  outputStyle: 'compressed', // expanded, compressed, compact
                },
              },
            },
          ],
        },
      ],
    },
    plugins: [
      new CleanWebpackPlugin({
        // Simulate the removal of files, default: false
        dry: false,
        // Write Logs to Console, (Always enabled when dry is true) , default: false
        verbose: true,
        // Automatically remove all unused webpack assets on rebuild, default: true
        cleanStaleWebpackAssets: false,
        // Do not allow removal of current webpack assets, default: true
        protectWebpackAssets: false,
        // default: ['**/*'] disables cleanOnceBeforeBuildPatterns
        cleanOnceBeforeBuildPatterns: [
          path.resolve(__dirname, '../dist/main.*.js'),
          path.resolve(__dirname, '../dist/manifest.*.js')
        ],
        // Removes files after every build (including watch mode) that match this pattern, default: []
        cleanAfterEveryBuildPatterns: ['static*.*', '!static1.js'],
        // Allow clean patterns outside of process.cwd()
        dangerouslyAllowCleanPatternsOutsideProject: true
      }),
      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, 'src/index.html'), //source
        filename: 'index.html',  //destination
        inject: true
      }),
      new MiniCssExtractPlugin({
        filename: 'paramita.min.css',
        chunkFilename: '[id].css',
      }),
    ],
  };
};
