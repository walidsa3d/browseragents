# BrowserAgents
![Build](https://travis-ci.org/walidsa3d/browseragents.svg?branch=master)
![downloads](https://img.shields.io/pypi/dm/browseragents.svg)
![license](https://img.shields.io/pypi/l/browseragents.svg)
![version](https://img.shields.io/pypi/v/browseragents.svg)

Generates a random browser user agent

# Install (automatic)
```
$ pip install browseragents
```
# Install (manual)
```
$ git clone git@github.com:walidsa3d/browseragents.git 
$ cd browseragents
$ python setup.py install
```
## Usage
```python
import browseragents as ba
ba.random()
//==> 'Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00'
ba.random(browser='firefox')
//==> 'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1'
ba.random(os='linux')
//==> 'Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1'
ba.random(browser='chrome', os='windows')
//==> 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
```
# License
```
The MIT License (MIT)

Copyright (c) 2015 Walid Saad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```