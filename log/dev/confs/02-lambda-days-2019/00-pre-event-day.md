# Day 0, 20.02.2019

Partial application and currying.

See:
* http://2ality.com/2011/09/currying-vs-part-eval.html
* https://fr.umio.us/favoring-curry/

## Partial application

Returns a function that takes a given argument `y` and returns a value of `f(x, y)`.

```js
const partApply = (f, x) => (y) => f(x, y);
const plus = (a, b) => a + b;
const plus2 = partApply(plus, 2);
const plus5 = plus.bind(null, 5); // native JS alternative

plus2(10); // 12
plus5(10); // 15
```

## Currying

All intermediate functions inside `curry(f)` return functions
and the last one returns an actual value of `f()` being applied to other arguments.

```js
const curry = (f) => (a) => (b) => (c) => f(a, b, c);
const sum = (...a) => a.reduce((acc, value) => acc + value, 0);

curry(sum)(10)(20)(30); // 60
```
