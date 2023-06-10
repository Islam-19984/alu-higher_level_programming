#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - i; i >= 0; i--) {
    const valueAtIndex = list[i];
    reversedList.push(valueAtIndex);
  }
  return reversedList;
};
