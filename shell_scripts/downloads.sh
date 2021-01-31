docker rm -f wiktionary-download;
docker run \
    --name=wiktionary-download \
    -v $1:"/word_list_directory_mount" \
    -v $2:"/target_directory_mount" \
    -v $3:"/cached_directory_mount" \
    alaverydev/audio-language-wiktionary-download