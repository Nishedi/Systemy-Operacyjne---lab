#!/bin/bash -eu

echo "1. "
grep -i "permission denied" ./fakaping.sh | sort -u | tee denied.log >&2

./fakaping.sh > /dev/null 2> >(sort >&2)


echo "3."
for file in "groovies"/*; do
  if [ -f "$file" ]; then
    sed -i '/Help docs:/d' "$file"
    sed -i 's/\$HEADER\$/\/temat\//g' "$file"
  fi
done



echo "4. "
cat yolo.csv | awk -F ',' '{if ($1 % 2 != 0) print $0}' >&2

cat yolo.csv | awk -F ',' '{gsub(/[$MB]/,"",$7); if ($7 == 2.99 || $7 == 5.99 || $7 == 9.99) print $2}'





