set term png
set output 'data.png'
stats "data.dat" u 1:2 nooutput
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 0
set style line 2 \
    linecolor rgb '#dd181f' \
    linetype 1 linewidth 2 \
    pointtype 5 pointsize 0
set title "Random Walk"
set xlabel "czas"
set ylabel "value"
set grid
unset key
plot "data.dat" u 1:2 with linespoints linestyle 2, \
    "linear.dat" u 1:2 with linespoints linestyle 1
quit