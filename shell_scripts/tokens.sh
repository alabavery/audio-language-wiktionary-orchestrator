docker run \
    --rm \
    --name=wiktionary-breakdown \
    -v $1:"/words_directory_mount" \
    -v $2:"/pages_directory_mount" \
    -v $3:"/target_directory_mount" \
    -e TARGET_LANGUAGE=$4 \
    alaverydev/audio-language-wiktionary-breakdown