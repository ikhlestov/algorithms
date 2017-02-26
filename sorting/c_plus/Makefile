CXX = g++
# -Wall - show all warnings
# -g - add the debugging information
CXXFLAGS = -Wall -g -std=c++11

# SOURCE_DIR = c_plus/

main: run_cplus_sort.o insertion.o selection.o utils.o
	$(CXX) $(CXXFLAGS) -o ../run_cplus_sort.out run_cplus_sort.o insertion.o selection.o utils.o

run_cplus_sort.o: run_cplus_sort.cpp insertion.o selection.o utils.o 
	$(CXX) $(CXXFLAGS) -c run_cplus_sort.cpp

insertion.o: insertion.h

selection.o: selection.h

utils.o: utils.h
