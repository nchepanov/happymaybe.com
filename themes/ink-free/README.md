# Happy Maybe Podcast Website

A conversational podcast where two friends share their insights on the winding journey of life.

Production site: [www.happymaybe.com](https://www.happymaybe.com/)

## Ink-Free

Crisp, minimal personal website and blog theme Hugo, designed for a collaborative, open-source, privacy conscious blog.

Forked from [knadh](https://github.com/knadh/hugo-ink) with custom adjustments. Originally forked from [Ezhil](https://github.com/vividvilla/ezhil).

### Run the example

```
cd happymaybe.com
hugo serve
```

```
hugo serve  --themesDir ../..
```

## Features
* Syntax highlighting
* RSS feeds
* Custom CSS/JS
* Multilingual months support
* Custom TOC
* In-Line images w/ Titles
* Random footer messages
* "Edit this on GitHub" button
* Word count, tags, and an approximate read time in the overview

## Installation

cd into your hugo site's root directory and:

```sh
cd themes
git submodule add https://github.com/chollinger93/ink-free 
```

For more information read the [official setup guide](https://gohugo.io/overview/installing/) of Hugo.


## Content type

You can specify content type with field `type` in your content. For example static pages can be set as type `page` which are excluded from recent posts and all posts page. You can use site params `mainSections` and `disableDisqusTypes` to control which page types are excluded from recent posts and Disqus comments respectively.

```md
---
title: "About"
date: 2019-04-19T21:37:58+05:30
type: "page"
---

This is some static page where you can write about yourself.
```

## Credits

* [knadh](https://github.com/knadh/hugo-ink), who created hugo-ink
* [Ezhil theme](https://github.com/vividvilla/ezhil) from which Ink was forked


## License
Licensed under the MIT license.
