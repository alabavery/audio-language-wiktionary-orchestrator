docker run \
    --rm \
    --name=populate-words-db \
    -v $1:"/combined_data_mt" \
    --network $2 \
    alaverydev/ninetypercentlanguage-populate-words-db \
    -db="$3"