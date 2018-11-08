/*
 * Util.cpp
 *
 *  Created on: Oct 31, 2018
 *      Author: Mark
 */
#include "Util.h"
int randInt(int lowerBound, int upperBound) {
	return ((double) rand() / (double) RAND_MAX) * (upperBound - lowerBound) + lowerBound;
}

vector<string> stringSplit(string rawString) {
	vector<string> strV;
	vector<int> splitList;
	string subStr;
	int i = 0;
	for(i = 0; i < rawString.length(); i++) {
		if (rawString.at(i) == '\'') {
			//cout << "found quote at " << i << endl;
			splitList.push_back(i);
		}
	}
	for (i = 0; i < splitList.size(); i+=2) {
		//cout << "i: " << i <<endl;
		//cout << "Start: " << splitList.at(i) << endl;
		//cout << "end: " << splitList.at(i+1) << endl;
		//cout << "Raw: " << rawString << endl;
		//cout << "Splice: " << rawString.substr(splitList.at(i), (splitList.at(i+1) - splitList.at(i))) << endl;
		subStr = rawString.substr(splitList.at(i), splitList.at(i+1) - splitList.at(i));
		if (subStr.at(0) == '\'') {
			subStr.erase(0,1);
		}
		//cout << subStr << endl;
		strV.push_back(subStr);
	}
	return strV;
}



