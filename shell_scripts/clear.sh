for folder in "$@"
    do
        echo "clearing $folder"
        sudo rm -rf $folder
        mkdir $folder
done