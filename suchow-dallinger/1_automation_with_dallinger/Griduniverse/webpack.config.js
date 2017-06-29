var webpack = require('webpack');
var BrowserSyncPlugin = require('browser-sync-webpack-plugin');
var UglifyJsPlugin = webpack.optimize.UglifyJsPlugin;
var env = process.env.WEBPACK_ENV;

var plugins = [];

if (env === 'build') {
  // set NODE_ENV=production in environment,
  // which ends up reducing size of React
  plugins.push(new webpack.DefinePlugin({'process.env': {'NODE_ENV': JSON.stringify('production')}}));
  // uglify code for production
  plugins.push(new UglifyJsPlugin({minimize: true}));
} else {
  plugins.push(new BrowserSyncPlugin({
    host: 'localhost',
    port: 6000,
    proxy: {
      target: 'http://localhost:5000',
      ws: true
    },
    serveStatic: [{
      route: '/static',
      dir: 'dlgr/griduniverse/static'
    }]
  }));
}

module.exports = {
  entry: {
    bundle: './dlgr/griduniverse/static/scripts/demo.js',
    questionnaire: './dlgr/griduniverse/static/scripts/questionnaire.js'
  },
  output: {
    path: __dirname + '/dlgr/griduniverse/static',
    filename: 'scripts/dist/[name].js'
  },
  // use jquery from separate script tag
  externals: { jquery: 'jQuery' },
  devtool: 'source-map',
  plugins: plugins
};
