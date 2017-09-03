##Important Note on Node Modules
Please note that since the multi-level-bloom-filter-js module is not published,
I've included the node modules in this repo. It's not clean (compared to
configuring this with npm), but it should be effective.

#To Use
1. Set the REVOKED and UNREVOKED constants in build_filter.js.
2. Set the REVOKED_FILENAME and UNREVOKED_FILENAME constants. 
3. `node build_filter.js --max-old-space-size=16384 > filter`
