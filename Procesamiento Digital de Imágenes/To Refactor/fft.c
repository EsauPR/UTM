/*
 *	Fast Fourier transform
 *	Example code obtained from http://rosettacode.org/wiki/Fast_Fourier_transform#C
 *	Added function ifft by Esaú
 *		@autor Esaú Peralta
 *		@email esau.opr@gmail.com
*/

#include <stdio.h>
#include <math.h>
#include <complex.h>

double PI;
typedef double complex cplx;

void _fft(cplx buf[], cplx out[], int n, int step)
{
	if (step < n) {
		_fft(out, buf, n, step * 2);
		_fft(out + step, buf + step, n, step * 2);

		for (int i = 0; i < n; i += 2 * step) {
			cplx t = cexp(-I * PI * i / n) * out[i + step];
			buf[i / 2]     = out[i] + t;
			buf[(i + n)/2] = out[i] - t;
		}
	}
}

void fft(cplx buf[], int n)
{
	cplx out[n];
	for (int i = 0; i < n; i++) out[i] = buf[i];

	_fft(buf, out, n, 1);
}

void ifft(cplx buf[], int n)
{
	for(int i = 0; i < n; i++)
		buf[i] = conj(buf[i]);

	fft(buf, n);

	for(int i = 0; i < n; i++){
		buf[i] = conj(buf[i]);
		buf[i] /= n;
	}
}


void show(const char * s, cplx buf[]) {
	printf("%s", s);
	for (int i = 0; i < 8; i++)
		if (!cimag(buf[i]))
			printf("(%g, 0)", creal(buf[i]));
		else
			printf("(%g, %g) ", creal(buf[i]), cimag(buf[i]));
    puts("");
}

int main()
{
	PI = atan2(1, 1) * 4;
	cplx buf[] = {1, 1, 1, 1, 0, 0, 0, 0};

	show("Data: ", buf);
	fft(buf, 8);
	show("FFT", buf);
	ifft(buf, 8);
	show("iFFT", buf);
}
