echo 'L         Teff'>LTeff3.dat
grep 'L,TE' pmsstar3.lst | awk '{print $5, $6}' >>LTeff3.dat
perl -pi -e 's/D/E/g' LTeff3.dat

echo 'L         Teff'>LTeff10.dat
grep 'L,TE' pmsstar10.lst | awk '{print $5, $6}' >>LTeff10.dat
perl -pi -e 's/D/E/g' LTeff10.dat

echo 'L         Teff'>LTeff1.dat
grep 'L,TE' pmsstar1.lst | awk '{print $5, $6}' >>LTeff1.dat
perl -pi -e 's/D/E/g' LTeff1.dat

echo 'L         Teff'>LTeff5.dat
grep 'L,TE' pmsstar5.lst | awk '{print $5, $6}' >>LTeff5.dat
perl -pi -e 's/D/E/g' LTeff5.dat
