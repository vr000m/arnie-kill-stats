gnuplot << EOF
set terminal pdf color enhanced rounded size 12,6 fname 'Times' fsize 12
set output "graph_movie.pdf"
set datafile separator "\t"
set origin 0,0
set border 3 lc rgb "black" lw 5
set grid
set size ratio 0.5
set key top left inside vertical font ",14"
set pointsize 2.5
set yrange [0:]
# set y2range [0:120]

# set xlabel "Years"
set ylabel "kills"
set xtics rotate by -270 font ",12"
# set logscale y 

# set xdata time
# set timefmt “%Y”

#set style data histogram
set style histogram cluster gap 1
set style fill solid 0.5 border
#pattern 5 noborder #
set boxwidth 0

titl = system("echo kills/movie")

plot "_movie.log" using 2:xtic(1) w histogram fs pattern 1 lc 1 lw 4 title titl
EOF
