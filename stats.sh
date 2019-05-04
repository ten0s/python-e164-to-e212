#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: stats.sh CSV_FILE"
    exit 1
fi

FILE="$1"

function countries() {
    # sort countries by freqs desc
    tail -n+2 "$FILE" | cut -d';' -f5,7 | sort | uniq | cut -d';' -f2 | sort | uniq -c | sort -nr | awk '{print $2}'
}

function filter_country() {
    country="$1"
    tail -n+2 "$FILE" | grep "$country" | cut -d';' -f5 | sort | uniq > "$country".txt
}

echo "| Country | Total | No Name | No ID |"
echo "|   ---   |  ---  |   ---   |  ---  |"
for country in $(countries); do
    filter_country "$country"
    python3 e164_to_e212.py -f "$country".txt > "$country"_res.txt
    total=$(grep -c "" "$country".txt)
    no_name=$(grep -c "!name" "$country"_res.txt)
    no_id=$(grep -c "!id" "$country"_res.txt)
    echo "| $country | $total | $no_name | $no_id |"
    rm -f "$country".txt "$country"_res.txt
done
