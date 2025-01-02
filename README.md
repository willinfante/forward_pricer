# forward_pricer

This is a very basic FX forward points calculator that I created from what I learned in the Lehman Brothers FX Training Manual. I did not include any quote fetching part in the code since it is meant for the user to use whichever quote they would like to calculate the points/forward rate. 

You can also calculate a forward rate from a bid-ask spread like: 1.4023/26. That part of the code still needs to be tested more to ensure it works with a variety of different pip sizes. I am still unsure of how to set up the bid-ask quote when the points are subtracted (dominant rate greater than minor rate) - I assumed that the points are apllied to the bid-ask from the spot and then flipped, but this is something I need to do more research on. I also need to fix the output for number of decimal places when the # of decimal places in is smaller than those that should go out (as of now the output decimal places is rounded to the beginning decimal places)
