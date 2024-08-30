set terminal wxt enhanced font ",12" background rgb "gray"
set xrange [0:100]
set yrange [0:100]
set zrange [0:100]
set xlabel "R"
set ylabel "G"
set zlabel "B"

splot 'data_blue.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "blue" title "Blue", \
      'data_brown.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "brown" title "Brown", \
      'data_black.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "black" title "Black", \
      'data_green.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "green" title "Green", \
      'data_red.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "red" title "Red", \
      'data_white.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "white" title "White", \
      'data_yellow.dat' using 1:2:3 with points pointtype 7 pointsize 1 lc rgb "yellow" title "Yellow"
