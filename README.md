# kakuyomuDownloader

A simple python app permitting to batch download novel chapters from kakuyomu.jp

### instructions
* launch with 'python kakuyomu.py'
* enter the serie number when asked (without spaces)
* wait
* you're done gj

<br>
e.g. for the novel 'https://kakuyomu.jp/works/1177354054880238351', the input is '1177354054880238351'

### issues
* superposed sentences are separated as "bottom sentence//top sentence"
* html errors aren't caught (the app will crash as is at the first error encountered)
* hasn't been tested on other novels, may have title problems
