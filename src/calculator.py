in calculator.c:	
double power(double a, int b) {
    double result = 1;

    if (b < 0) {
        b = -b;

        for (int i = 0; i < b; i++) {
            result *= a;
        }

        return 1 / result;
    }

    for (int i = 0; i < b; i++) {
        result *= a;
    }

    return result;
}


main:
printf("Power: %.2f\n", power(a, b));