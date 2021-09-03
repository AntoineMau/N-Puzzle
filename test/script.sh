#!/bin/bash

file_name='tmp-3-'
file_exte='.txt'
algo=('astar' 'greedy' 'uniform')
heur=('manhattan' 'hamming' 'euclidean')

GREEN='\033[0;32m'
NC='\033[0m'
CHECK=${GREEN}'\u2714'${NC}
j=0

printf "Creating n-puzzle files "
for i in {1..100}
do
	tab[$i-1]=`printf "$file_name%03d$file_exte" "$i"`
done

for i in ${tab[*]}
do
	python3 ../generator.py 3 > $i
done
printf " ${CHECK}\n"

printf "\nRunning n-puzzle program\n"
echo "File name;Algorithm name;Heuristic name;Complexity time;Complexity size;Number of moves;Time" > test.csv
for i in ${tab[*]}
do
	printf "$i"
	for a in ${algo[*]}
	do
		for h in ${heur[*]}
		do
			echo "$i;$a;$h;`timeout 10 python3 ../main.py -F $i -A $a -H $h || echo "0;0;0;0"`" >> test.csv
			printf " ${CHECK}"
		done
	done
	printf "\n"
done
