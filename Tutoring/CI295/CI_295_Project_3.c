#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CLOCKS_PER_MILLI (CLOCKS_PER_SEC / 1000)
#define TESTLENGTH 20
#define COLUMNS 5
#define TRIALS 5
#define STARTLEN 1000
#define MAXLEN 100000
#define JUMP 500

void fillRandom(int array[], int length, int lowerBound, int upperBound);
void arrayCopy(int source[], int destination[], int sourceLen, int destLen);
void insertionSort(int array[], int length);
void printArray(const int array[], int length, int columns);
int isSorted(const int array[], int length);
void merge(int firstArray[], int secondArray[], int destinationArray[],
		int firstLength, int secondLength, int destinationLength);
void mergeSort(int array[], int length);


int main() {
	/*variable declarations */
	clock_t startTime;
	clock_t endTime;
	int dataArray[MAXLEN];
	int dataCopy[MAXLEN];
	FILE* mergeSortFile;
	FILE* insertionSortFile;
	int i;
	int j;
	/* seeds the random number generator */
	srand(time(0));
	/* verification that both sorts work and the general concept is sound*/
	fillRandom(dataCopy, TESTLENGTH, 0, RAND_MAX);
	arrayCopy(dataCopy, dataArray, TESTLENGTH, TESTLENGTH);
	printf("Array before insertion sort:\n ");
	printArray(dataArray, TESTLENGTH, 5);
	insertionSort(dataArray, TESTLENGTH);
	printf("Array after insertionSort:\n");
	printArray(dataArray, TESTLENGTH, 5);
	if (isSorted(dataArray, TESTLENGTH)) {
		printf("The array is sorted by insertionSort, HURRAY!\n");
	} else {
		printf("InsertionSort did not sort the array, drat\n");
	}
	arrayCopy(dataCopy, dataArray, TESTLENGTH, TESTLENGTH);
	printf("Array before mergeSort: \n");
	printArray(dataArray, TESTLENGTH, COLUMNS);
	mergeSort(dataArray, TESTLENGTH);
	printf("Array after mergeSort: \n");
	printArray(dataArray, TESTLENGTH, COLUMNS);
	if (isSorted(dataArray, TESTLENGTH)) {
		printf("The array is sorted by MergeSort, HURRAY!\n");
	} else {
		printf("MergeSort did not sort the array, drat\n");
	}
	fflush(stdout);
	/*actual assignment portion*/
	insertionSortFile = fopen("insertion.csv", "w");
	mergeSortFile = fopen("merge.csv", "w");
	for(i = STARTLEN; i <= MAXLEN; i += JUMP ) {
		printf("running with length %d\n", i);
		fflush(stdout);
		fprintf(insertionSortFile, "%d,", i);
		fprintf(mergeSortFile, "%d,", i);
		fflush(mergeSortFile);
				fflush(insertionSortFile);
		for(j = 0; j < TRIALS; j++) {
			fillRandom(dataCopy, i, 0, RAND_MAX);
			arrayCopy(dataCopy, dataArray, i, i);
			startTime = clock();
			insertionSort(dataArray, i);
			endTime = clock();
			fprintf(insertionSortFile, "%7.2f,", ((double) (endTime - startTime) / ((double) CLOCKS_PER_MILLI)));
			arrayCopy(dataCopy, dataArray, i, i);
			startTime = clock();
			mergeSort(dataArray, i);
			endTime = clock();
			fprintf(mergeSortFile, "%7.2f,", ((double) (endTime - startTime) /((double) CLOCKS_PER_MILLI)));
		}
		fputc('\n', mergeSortFile);
		fputc('\n', insertionSortFile);
		fflush(mergeSortFile);
		fflush(insertionSortFile);
	}
	fclose(mergeSortFile);
	fclose(insertionSortFile);
	return 0;

}

/* fills an array of integers with random ints with [lower, upper] */
void fillRandom(int array[], int length, int lowerBound, int upperBound) {
	int i = 0;
	for (i = 0; i < length; i++) {
		/* the + 1 in the range is the change it from [lower, upper) to [lower, upper] */
		array[i] = rand() / ((double) RAND_MAX + 1)
						* (upperBound - lowerBound + 1) + (lowerBound);
	}
}

/* copies the source array into destination array, overwriting as we go */
void arrayCopy(int source[], int destination[], int sourceLen, int destLen) {
	int i = 0;
	for (i = 0; i < sourceLen && i < destLen; i++) {
		destination[i] = source[i];
	}
}

/* insertion sort from GeeksForGeeks*/
void insertionSort(int array[], int length) {
	int i, key, j;
	for (i = 1; i < length; i++) {
		key = array[i];
		j = i - 1;
		while (j >= 0 && array[j] > key) {
			array[j + 1] = array[j];
			j = j - 1;
		}
		array[j + 1] = key;
	}
}

/* prints an array */
void printArray(const int array[], int length, int columns) {
	int i = 0;
	for (i = 0; i < length; i++) {
		if ((i % columns) == 0 && i != 0) {
			printf("\n");
		}
		printf("%7d", array[i]);
	}
	printf("\n");
}

/* verifies an array is sorted from least to greatest*/
int isSorted(const int array[], int length) {
	int i = 0;
	for (i = 1; i < length; i++) {
		if (array[i] < array[i - 1]) {
			return 0;
		}
	}
	return 1;
}

void merge(int firstArray[], int secondArray[], int destinationArray[],
		int firstLength, int secondLength, int destinationLength) {
	int i = 0;
	int j = 0;
	int k = 0;
	int* temp = malloc((firstLength + secondLength) * sizeof(int));
	while (i < firstLength && j < secondLength && k < destinationLength) {
		if (firstArray[i] < secondArray[j]) {
			temp[k] = firstArray[i];
			++i;
		} else {
			temp[k] = secondArray[j];
			++j;
		}
		++k;
	}
	while (i < firstLength && k < destinationLength) {
		temp[k++] = firstArray[i++];
	}
	while (j < secondLength && k < destinationLength) {
		temp[k++] = secondArray[j++];
	}
	arrayCopy(temp, destinationArray, k, destinationLength);
	free(temp);
}

void mergeSort(int array[], int length) {
	int mid = length / 2;
	int* middlePoint = &array[mid];

	if (length == 1) {
		return;
	} else {
		mergeSort(array, mid);
		mergeSort(middlePoint, length - mid);
		merge(array, middlePoint, array, mid, length - mid, length);
	}
}
