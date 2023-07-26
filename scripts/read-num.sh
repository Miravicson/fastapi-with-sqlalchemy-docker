#!/bin/sh

echo "Please enter a number: "
read num

if [[$num -gt 0]]; then
  echo "$num is positive"
elif [[$num -lt 0]]; then
  echo "$num is negative"
else
  echo "$num is Zero"
fi

i=1
while [[ $i -le 10 ]]; do
  echo "$i"
  ( (i += 1))
done
