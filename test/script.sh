#!/bin/bash

file_name='tmp-3-'
file_exte='.txt'
algo=('astar' 'greedy' 'uniform')
heur=('manhattan' 'hamming' 'euclidean')
i_resul=0

for i in {1..10}
do
	tab[$i-1]="$file_name$i$file_exte"
done

for i in ${tab[*]}
do
	python3 ../generator.py 3 > $i
done

echo "File name;Algorithm name;Heuristic name;Complexity time;Complexity size;Number of moves;Time" > test.csv

for i in ${tab[*]}
do
	printf "%12s\n" "$i"
	for a in ${algo[*]}
	do
		printf "%20s\n" "$a"
		for h in ${heur[*]}
		do
			echo "$i;$a;$h;`python3 ../main.py -F $i -A $a -H $h`" >> test.csv
			printf "%30s%5s\n" "$h" "DONE"
		done
	done
done
