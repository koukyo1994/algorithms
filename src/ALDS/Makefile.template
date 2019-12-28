FILE := MaximumProfit
CASE := case1

compile:
	g++ -o out/${FILE} ${FILE}.cpp

run:
	./out/${FILE} < test/${CASE}/input.txt > test/${CASE}/${FILE}.txt
	diff test/${CASE}/answer.txt test/${CASE}/${FILE}.txt
