# JaVieScript

## Description
Something something JS something

Author: vie.pls

## Attachments
[checker.js](./Challenge/checker.js)
[index.html](./Challenge/index.html)

## Solution
This challenge is really great and fun javascript puzzle challenge. 
To solve this challenge, first let's see the source code of `checker.js`

```js
var flag = "maple{";
var honk = {};

async function hash(string) {
	const utf8 = new TextEncoder().encode(string);
	const hashBuffer = await crypto.subtle.digest('SHA-256', utf8);
	const hashArray = Array.from(new Uint8Array(hashBuffer));
	const hashHex = hashArray
	  .map((bytes) => bytes.toString(16).padStart(2, '0'))
	  .join('');
	return hashHex;
  }

async function constructflag() {
	const urlParams = new URLSearchParams(window.location.search);
	var fleg = "maple{";
	for (const pair of urlParams.entries()) {
		honk[pair[0]] = JSON.parse(pair[1]); 
	}

	if (honk.toString() === {}.toString()) {
		fleg += honk.toString()[9];
	}

	if (Object.keys(honk).length === 0) {
		const test = eval(honk.one);
		if (typeof test === 'number' && test * test + '' == test + '' && !/\d/.test(test)) {
			fleg += 'a' + test.toString()[0];
		}

		const quack = honk.two;

		if (quack.toString().length === 0 & quack.length === 1) {
			fleg += 'a' + (quack[0] + '')[0].repeat(4) + 'as';
		}

		const hiss = honk.three;

		if (hiss === "_are_a_mId_FruiT}") {
			fleg += hiss;
		}
	}
	if (await hash(fleg) == "bfe06d1e92942a0eca51881a879a0a9aef3fe75acaece04877eb0a26ceb8710d") {
		console.log(fleg);
	}
}

constructflag();
```

From the source code there is `constructflag()` function to create the flag and the `hash()` function is use to verify our flag with the SHA256 of the real flag.
If we look at `constructflag()` function there are few points to notes here:
- The function will get our URL query as parameter.
- First part of the flag is stored in `fleg` variable.
- From our URL query it will check if the stored URL parameters is an empty object. If yes it will store the index 9 of the string to `fleg`.
- The second condition will check if the `honk` object is an empty object.
- And then there will be nested if conditions inside the second condition. It will check if `test` is a number, the value of `test * test + '' == test + ''`, and `test` cannot contain any digits or numerical values. If conditions is met then it will add `a` character and add the first index of `test` to `fleg`.
- Third if conditions will check if `quack.toString().length === 0` and `quack.length === 1` is true. If yes, then `a` character will be added to `fleg`, repeat the first index of `quack` four times, and add with `as` character to `fleg`.
- The fourth condition will check if `hiss` contains `_are_a_mId_FruiT}` and if it true then `_are_a_mId_FruiT}` is added to `fleg`.
- The last condition will check if `fleg` is equal to given SHA256 sum.

Okay, so how do we solve the puzzle in this challenge?
The first step is by declaring an empty object. We can try this code to make sure it will meet the first condition.

```js
var fleg = "maple{";
var honk = {};
    
if (honk.toString() === {}.toString()) {
	fleg += honk.toString()[9];
}
console.log(fleg);
```

Then we will get the output is `maple{b`.

The second if condition and the nested if inside that condition is little bit tricky in here.
From the first step we already met the condition of the second if condition, but you need to think about how to meet the if condition inside the second if condition.
From [w3schools](https://www.w3schools.com/js/js_numbers.asp) we know that in Javascript there are variable or object with the type is `number` but without using any numeric values, the possible value is `NaN` or `Inifinity`.
But the best value to make the flag more makes sense is `NaN`, because we already know that `_are_a_mId_FruiT}` is part of the flag then we just need to find the fruit in this flag. 
Which is `NaN` is the most fit value because we will get something like this `maple{baN`. But if we use `Infinity` it will become `maple{baI` and there's no fruit name that is start with bai.
This is the code for satisfy the second if condition and the nested if condition.

```js
var fleg = "maple{";
var honk = {};
    
if (honk.toString() === {}.toString()) {
	fleg += honk.toString()[9];
}

if (Object.keys(honk).length === 0) {
	honk.one = NaN;
	const test = eval(honk.one);
	if (typeof test === 'number' && test * test + '' == test + '' && !/\d/.test(test)) {
		fleg += 'a' + test.toString()[0];
	}
}
console.log(fleg);
```

For the third condition, we need to use Javascript type coercion to meet this condition.
We will use an array that will define it's value as empty. There are 3 canditates for the value of this array, `['']`, `[null]`, and `[undefined]`.
But `[null]` is the best value for the third condition, because we will get banana as the fruit name in this flag.
This is the code for the third condition.

```js
var fleg = "maple{";
var honk = {};
    
if (honk.toString() === {}.toString()) {
	fleg += honk.toString()[9];
}

if (Object.keys(honk).length === 0) {
	honk.one = NaN;
	const test = eval(honk.one);
	if (typeof test === 'number' && test * test + '' == test + '' && !/\d/.test(test)) {
		fleg += 'a' + test.toString()[0];
	}
}

honk.two = [null];
const quack = honk.two;
if (quack.toString().length === 0 & quack.length === 1) {
	fleg += 'a' + (quack[0] + '')[0].repeat(4) + 'as';
}
console.log(fleg);
```

The last condition is easy, because we just need to assign `_are_a_mId_FruiT}` value to `honk.three`.
The code for the last condition.

```js
var fleg = "maple{";
var honk = {};
    
if (honk.toString() === {}.toString()) {
	fleg += honk.toString()[9];
}

if (Object.keys(honk).length === 0) {
	honk.one = NaN;
	const test = eval(honk.one);
	if (typeof test === 'number' && test * test + '' == test + '' && !/\d/.test(test)) {
		fleg += 'a' + test.toString()[0];
	}
}

honk.two = [null];
const quack = honk.two;
if (quack.toString().length === 0 & quack.length === 1) {
	fleg += 'a' + (quack[0] + '')[0].repeat(4) + 'as';
}

honk.three = "_are_a_mId_FruiT}";
const hiss = honk.three;

if (hiss === "_are_a_mId_FruiT}") {
  fleg += hiss;
}
console.log(fleg);
```

For the complete code you can see at [solver.js](./solver.js).
Run the code using web browser by editing Javascript code using `solver.js` and the flag will be printed in Console.

![Flag](./flag.png)

## Flag
`maple{baNannnnas_are_a_mId_FruiT}`
