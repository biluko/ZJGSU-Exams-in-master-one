proc cancorr data=sasuser.examp1032(type=corr) vprefix=u wprefix=v;
   var x1-x5;
   with y1-y7;
run;
