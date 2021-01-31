docker rm -f wiktionary-definition;
docker run \
    --name=wiktionary-definition \
    -v $1:"/source_directory_mount" \
    -v $2:"/target_directory_mount" \
    alaverydev/audio-language-wiktionary-definition