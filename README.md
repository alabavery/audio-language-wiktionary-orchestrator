**list of words and working directory**
</br>|</br>|</br>v</br>
[wiktionary-download](https://github.com/alabavery/audio-language-wiktionary-download)              f
</br>|</br>|</br>v</br>
**downloaded pages**
</br>|</br>|</br>v</br>
[wiktionary-breakdown](https://github.com/alabavery/audio-language-wiktionary-breakdown)
</br>|</br>|</br>v</br>
**tokens json files (each section of the targeted language divided by line into array)**
</br>|</br>|</br>v</br>
[wiktionary-lemmas](https://github.com/alabavery/audio-language-wiktionary-lemmas)
</br>|</br>|</br>v</br>
**lemmas json files**
</br>|</br>|</br>v</br>
[lemma-regroup](https://github.com/alabavery/audio-language-wiktionary-orchestrator/blob/master/functions/lemma_regroup.py) (re-runs download and breakdown for the lemmas, adding to the already created downloads and tokens directories)
</br>|</br>|</br>v</br>
[wiktionary-definitions](https://github.com/alabavery/audio-language-wiktionary-definitions)
</br>|</br>|</br>v</br>
**definitions json**
</br>|</br>|</br>v</br>
[wiktionary-combine](https://github.com/alabavery/audio-language-wiktionary-combine)
</br>|</br>|</br>v</br>
**final json files, one for each word:**
```
[
    {
        "part_of_speech": string, // verb, adverb e.g.
        "lemmas": [
            "word": string, // lemma for word and part of speech (usually there is just one),
            "definitions": []string, // the definitions of said lemma
        ]
    }
]
```