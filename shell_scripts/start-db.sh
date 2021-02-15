docker run \
    --rm \
    --name $1 \
    -e POSTGRES_PASSWORD=$2 \
    -e POSTGRES_USER=$3 \
    -e POSTGRES_DB=$4 \
    -d \
    --network $5 \
    postgres;
