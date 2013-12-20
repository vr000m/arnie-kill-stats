#plotting bitrate.txt using gnuplot
gnuplot << EOF
name=system("echo skills") 
set terminal pdf color enhanced rounded size 12,6 fname 'Times' fsize 24
set output "graph_skills.pdf"
set origin 0,0
set border 3 lc rgb "black" lw 5
set grid
set size ratio 0.5
set key right inside vertical font ",18"
set pointsize 2.5
set yrange [0:]
# set y2range [0:120]

set xlabel "Years"
set ylabel "kills"
set xtics rotate by -270
set datafile missing "-"
# set logscale y 

# set xdata time
# set timefmt “%Y”
# set format x "%Y"

#set style data histogram
set style data histogram
set style histogram rowstacked
# set style histogram cluster gap 1
set style fill solid 0.5 border
#pattern 5 noborder #
set boxwidth 0

plot "_sk_strength.log" using 2:xtic(1) w histogram fs lw 4 title "strength" , \
"_sk_guns.log" using 2:xtic(1) w histogram fs lw 4 title "guns" , \
"_sk_driving.log" using 2:xtic(1)  w histogram fs lw 4 title "driving", \
"_sk_bombs.log" using 2:xtic(1)  w histogram fs lw 4 title "explosions", \
"_sk_swords.log" using 2:xtic(1)  w histogram fs lw 4 title "swords"
EOF