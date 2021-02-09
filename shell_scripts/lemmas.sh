docker run \
    --rm \
    --name=wiktionary-lemma \
    -v $1:"/wds_dir_mt" \
    -v $2:"/toks_dir_mt" \
    -v $3:"/tgt_dir_mt" \
    -e TARGET_LANGUAGE=$4 \
    alaverydev/audio-language-wiktionary-lemma