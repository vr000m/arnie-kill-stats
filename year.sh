#plotting bitrate.txt using gnuplot
gnuplot << EOF
name=system("echo $1") 
set terminal pdf color enhanced rounded size 12,6 fname 'Times' fsize 24
set output "graph".name.".pdf"
set origin 0,0
set border 3 lc rgb "black" lw 5
set grid
set size ratio 0.5
set key top left inside horizontal font ",18"
set pointsize 2.5
set yrange [0:]
# set y2range [0:120]

set xlabel "Years"
set ylabel "kills"
set xtics rotate by -270
# set logscale y 

# set xdata time
# set timefmt “%Y”

#set style data histogram
set style histogram cluster gap 1
set style fill solid 0.5 border
#pattern 5 noborder #
set boxwidth 0

titl = system("echo kills/year")

plot "$1.log" using 2:xtic(1) w histogram fs pattern 1 lc 1 lw 4 title titl
EOF