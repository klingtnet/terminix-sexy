# [terminal.sexy](http://terminal.sexy/) for [terminix](https://github.com/gnunn1/terminix)

This is a little python script that converts JSON formatted color schemes from [terminal.sexy](http://terminal.sexy/) to the JSON format that is used in terminix.

## Quickstart

```sh
git clone --recursive url/of/this/repo/terminix.sexy.git
make
```

If your terminix scheme path is not `/usr/share/terminix/schemes` call make like this:

```sh
TERMINIX_SCHEME_PATH='/path/to/terminix/schemes' make
```

## Requirements

- python 3.x
- gnu make
