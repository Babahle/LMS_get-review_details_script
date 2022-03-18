review_id="/\(([^)]+)\)/gm"

wtc-lms reviews | grep -i assigned | while read line; do
    echo $(wtc-lms accept $(python3 get_ids.py $line))
done
