#!/bin/bash

size=3
nb_file=10
file_name='npuzzle-'$size'-'
file_exte='.txt'
algo=('astar' 'greedy' 'uniform')
heur=('manhattan' 'hamming' 'euclidean')

GREEN='\033[0;32m'
NC='\033[0m'
CHECK=${GREEN}'\u2714'${NC}

if [ $1 ]
then
	nb_file=$1
fi

printf "Creating n-puzzle files "
for i in $(seq 1 ${nb_file})
do
	tab[$i-1]=`printf "$file_name%03d$file_exte" "$i"`
done

for i in ${tab[*]}
do
	python3 ../generator.py -s 1000 $size > $i
done
printf " ${CHECK}\n"

printf "\nRunning n-puzzle program\n"
echo "File name;Algorithm name;Heuristic name;Complexity time;Complexity size;Number of moves;Time" > npuzzle.csv
for i in ${tab[*]}
do
	printf "$i"
	for a in ${algo[*]}
	do
		for h in ${heur[*]}
		do
			echo "$i;$a;$h;`timeout 20 python3 ../main.py -S $i -A $a -H $h || echo "0;0;0;0"`" >> npuzzle.csv
			printf " ${CHECK}"
		done
	done
	printf "\n"
done
