# plot all skill fatalities
for f in _sk_*.log; 
do 
	m=$(echo $f | rev | cut -c 5- | rev)
	n=$(echo $m | cut -c 5-)
	echo "Processing $n file..";
	#source plot.sh $m
	source rect.sh $m $n
done
