CXX = g++
# -Wall - show all warnings
# -g - add the debugging information
CXXFLAGS = -Wall -g -std=c++11

# SOURCE_DIR = c_plus/

main: run_cplus_sort.o insertion.o selection.o utils.o merge.o bubble.o
	$(CXX) $(CXXFLAGS) -o ../run_cplus_sort.out run_cplus_sort.o insertion.o selection.o utils.o merge.o bubble.o

run_cplus_sort.o: run_cplus_sort.cpp insertion.o selection.o utils.o merge.o bubble.o
	$(CXX) $(CXXFLAGS) -c run_cplus_sort.cpp

insertion.o: insertion.h

selection.o: selection.h

merge.o: merge.h

bubble.o: bubble.h

utils.o: utils.h
