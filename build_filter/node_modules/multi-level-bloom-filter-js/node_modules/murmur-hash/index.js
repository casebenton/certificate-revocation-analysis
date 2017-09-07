'use strict';

module.exports =  {
  v3: require('./lib/v3')
};

// -- Test Code ---------------------------------------------------------
if (require.main === module) {
  (function () {
    console.log(module.exports.v3);
  })();
}
