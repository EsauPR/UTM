clear all;
s0 = load("in1");
s1 = load("sal1");

t1 = [1:size(s0)];
t2 = [1:size(s1)];

figure; plot(s0);
figure; plot(s1);

figure; plot(t1, s0, t2, s1);

e = load("error1");
figure; plot(e);
