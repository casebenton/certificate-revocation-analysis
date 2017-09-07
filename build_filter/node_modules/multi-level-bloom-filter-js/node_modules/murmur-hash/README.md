# Murmur Hash (v3)
A javascript implementation of [MurmurHash3](https://code.google.com/p/smhasher/source/browse/trunk/MurmurHash3.cpp?spec=svn145&r=144)'s hashing algorithms.

### Installation
```
$ npm install murmur-hash
```

### Usage
```
var murmurHash3 = require('murmur-hash').v3;
```

### Examples

```
// Return a 32bit hash as a unsigned int:
> murmurHash3.x86.hash32("I will not buy this record, it is scratched.")
  2832214938

// Return a 128bit hash as a unsigned hex:
> murmurHash3.x86.hash128("I will not buy this tobacconist's, it is scratched.")
  "9b5b7ba2ef3f7866889adeaf00f3f98e"
> murmurHash3.x64.hash128("I will not buy this tobacconist's, it is scratched.")
  "d30654abbd8227e367d73523f0079673"

// Specify a seed (defaults to 0):
> murmurHash3.x86.hash32("My hovercraft is full of eels.", 25)
  2520298415
```
