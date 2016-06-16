#! /bin/octave -qf
printf ("%s", program_name ());
arg_list = argv ();


m = imread(arg_list{1} , "jpg");

save "img_tmp";
