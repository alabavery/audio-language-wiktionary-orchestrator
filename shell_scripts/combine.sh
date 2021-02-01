docker rm -f wiktionary-combine;
docker run \
    --name=wiktionary-combine \
    -v $1:"/wds_dir_mt" \
    -v $2:"/def_dir_mt" \
    -v $3:"/lemma_dir_mt" \
    -v $4:"/tgt_dir_mt" \
    alaverydev/audio-language-wiktionary-combine