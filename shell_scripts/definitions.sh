docker run \
    --rm \
    --name=wiktionary-definition \
    -v $1:"/source_directory_mount" \
    -v $2:"/target_directory_mount" \
    alaverydev/audio-language-wiktionary-definition