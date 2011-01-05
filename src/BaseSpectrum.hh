/*
  Copyright (c) 2011 Timothy Lovorn

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
*/

#ifndef __SCSS_BASE_SPECTRUM_H
#define __SCSS_BASE_SPECTRUM_H

#include <cmath>

#include "BaseState.hh"

class BaseSpectrum {
public:
    BaseSpectrum(const BaseState& _st);
    // One-hole spectrum to be used, minimum at 0
    double epsilon(double kx, double ky);
    // One-hole spectrum unmodified from theory
    double epsilonBar(double kx, double ky);
    // One-hole energy, epsilon - mu
    double xi(double kx, double ky);
protected:
    const BaseState& st;
};

#endif
