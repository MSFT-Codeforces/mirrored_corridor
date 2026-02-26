#include <algorithm>
#include <iostream>
#include <numeric>

using SignedInt128 = __int128_t;

static const long long kInfinity = 4000000000000000000LL;

/**
 * @brief Normalizes a value into the range [0, modulus-1] for modulus > 0.
 *
 * @param value The value to normalize.
 * @param modulus The positive modulus.
 * @return The normalized remainder in [0, modulus-1].
 */
long long normalizeModulo(long long value, long long modulus) {
    long long remainder = value % modulus;
    if (remainder < 0) {
        remainder += modulus;
    }
    return remainder;
}

/**
 * @brief Computes gcd(firstValue, secondValue) and finds coefficients x,y such that:
 *        firstValue * x + secondValue * y = gcd(firstValue, secondValue).
 *
 * @param firstValue The first integer.
 * @param secondValue The second integer.
 * @param coefficientX Output coefficient for firstValue.
 * @param coefficientY Output coefficient for secondValue.
 * @return The gcd of firstValue and secondValue.
 */
long long extendedGcd(long long firstValue, long long secondValue, long long &coefficientX, long long &coefficientY) {
    if (secondValue == 0) {
        coefficientX = 1;
        coefficientY = 0;
        return firstValue;
    }

    long long nextX = 0;
    long long nextY = 0;
    long long gcdValue = extendedGcd(secondValue, firstValue % secondValue, nextX, nextY);

    coefficientX = nextY;
    SignedInt128 updatedY = (SignedInt128)nextX - (SignedInt128)(firstValue / secondValue) * (SignedInt128)nextY;
    coefficientY = (long long)updatedY;

    return gcdValue;
}

/**
 * @brief Computes the modular inverse of value modulo modulus, assuming gcd(value, modulus) = 1.
 *
 * @param value The value to invert.
 * @param modulus The modulus (positive).
 * @return inverseValue such that (value * inverseValue) % modulus == 1.
 */
long long modularInverse(long long value, long long modulus) {
    long long coefficientX = 0;
    long long coefficientY = 0;
    extendedGcd(value, modulus, coefficientX, coefficientY);

    coefficientX %= modulus;
    if (coefficientX < 0) {
        coefficientX += modulus;
    }
    return coefficientX;
}

/**
 * @brief Computes the minimum number of presses to reach targetRemainder from startRemainder
 *        on the cycle Z_cycleLength, moving by +/- stepSize each press.
 *
 * @param cycleLength The modulus L (must be > 0).
 * @param stepSize The step size d.
 * @param startRemainder The starting remainder in [0, cycleLength-1].
 * @param targetRemainder The target remainder in [0, cycleLength-1].
 * @return The minimum presses, or kInfinity if unreachable.
 */
long long minimumPressesToReachRemainder(long long cycleLength,
                                        long long stepSize,
                                        long long startRemainder,
                                        long long targetRemainder) {
    stepSize = normalizeModulo(stepSize, cycleLength);

    long long difference = normalizeModulo(targetRemainder - startRemainder, cycleLength);
    if (difference == 0) {
        return 0;
    }
    if (stepSize == 0) {
        return kInfinity;
    }

    long long gcdValue = std::gcd(cycleLength, stepSize);
    if (difference % gcdValue != 0) {
        return kInfinity;
    }

    long long reducedModulus = cycleLength / gcdValue;
    long long reducedStep = stepSize / gcdValue;
    long long reducedDifference = difference / gcdValue;

    if (reducedModulus == 1) {
        return 0;
    }

    long long inverseStep = modularInverse(normalizeModulo(reducedStep, reducedModulus), reducedModulus);
    long long forwardSteps = (long long)((SignedInt128)reducedDifference * inverseStep % reducedModulus);

    return std::min(forwardSteps, reducedModulus - forwardSteps);
}

/**
 * @brief Reads test cases and prints the minimum number of button presses for each case.
 *
 * @return 0 on successful execution.
 */
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int testCaseCount = 0;
    std::cin >> testCaseCount;

    for (int testCaseIndex = 0; testCaseIndex < testCaseCount; ++testCaseIndex) {
        long long roomCount = 0;
        long long startRoom = 0;
        long long targetRoom = 0;
        long long stepSize = 0;
        std::cin >> roomCount >> startRoom >> targetRoom >> stepSize;

        if (roomCount == 1) {
            std::cout << 0 << "\n";
            continue;
        }

        long long cycleLength = 2 * (roomCount - 1);
        long long startRemainder = startRoom - 1;
        long long targetCoordinate = targetRoom - 1;

        long long targetRemainderDirect = targetCoordinate;
        long long targetRemainderMirror = (cycleLength - targetCoordinate) % cycleLength;

        long long bestAnswer = kInfinity;
        bestAnswer = std::min(bestAnswer,
                              minimumPressesToReachRemainder(cycleLength, stepSize, startRemainder, targetRemainderDirect));
        bestAnswer = std::min(bestAnswer,
                              minimumPressesToReachRemainder(cycleLength, stepSize, startRemainder, targetRemainderMirror));

        if (bestAnswer >= kInfinity / 2) {
            bestAnswer = -1;
        }

        std::cout << bestAnswer << "\n";
    }

    return 0;
}