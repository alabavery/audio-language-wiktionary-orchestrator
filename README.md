### Final output is
- create files that contain
{
    word,
    parts_of_speech: [{
        name: string,
        lemmas: string[],
        definitions: string[],
        datapoints: [{
            name: string,
            data: { [key: string]: any },
        }]
    }]
}
