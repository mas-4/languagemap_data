# Language Map Data Repository

To see the program in action visit langmap.netlify.app

## About
This is the data for langmap.netlify.app. It is free for anyone to use or
modify.

This data was scraped from the [List of countries by spoken languages][0] on
Wikipedia. It was a horrifically badly formatted page, and I thus spent a good
deal of time aggregating it using Python, [gspread][1], the Google Drive/Sheets
API, and Google Sheets' `=importHTML()` function. It was by no means automated,
and I had to concatenate and label a lot of things by hand, specifically in
normalizing the status of each language within each country. Below is a series
of general rules of thumb I took as I went through the list.

## General Rules I Chose
- co-official, official or minority in [place] = regional
- spoken in <place> = regional
- co-official = official
- de facto, unofficial = de facto
- de facto, official = official
- minority everywhere, official somewhere = minority
- official minority = minority
- de facto/more than 50% = de facto
- widely used, not official = de facto

## Apologia

Mistakes were made. Get over it. You want it fixed? Do it yourself. This data is
free to be cloned and adjusted.

## Call to Action

I normalized the status codes to a mere 10. I do not want more than there
already are. In fact, I would like to reduce the number. I understand that
languages are complex, but this project isn't meant to be a definitive resource,
it's just to give people a sense of how much of the world they can visit and
know the language in. Plus, I really don't know what the hell a naked
`unofficial` is, so I changed it based on what I guessed from Wikipedia. In
general, that Wikipedia page is horribly sourced and designed and if we can
contribute back to it by renormalizing into a single table it would be
incredible, I'm just not sure if it would be welcome.

## Current Statuses
The current statuses are listed below. I specifically would like to get rid of
`significant language`. It is the least clear. `Historical language` also
seems silly.

Below are what I assume are the definitions for the various status codes.

- `administrative language`: a language used only for administrative functions.
- `de facto`: a language that is spoken by the majority of the population even
  if it is not an official language.
- `historical language`: a language important to the history of the country.
- `majority`: honestly this is probably the same as de facto and needs
  elimination.
- `minority`: any language spoken by a minority of the population.
- `official`: a language that is officially recognized.
- `regional`: a language spoken in a region or regions, either by a minority in
  that region, or by a majority.
- `religious`: a religion mostly used for religious services.
- `significant language`: I have no idea.

## How to Contribute
The original status descriptions of the languages on the Wikipedia page are
visible in original_non-normalized.csv. If you have a good reason to change the
status of a row or group of rows, please do so in languages_final.csv and
explain the change in your commit/PR. The only sheet worth changing is that one
because it's the one from which I build the json file for langmap.netlify.app.

`languages_complete.csv` includes a good deal more languages than
`languages_final.csv`, and also doesn't reflect all of the changes in
`languages_final.csv`. That is because in it's current design too many languages
results in a serious lag on the page. Future renditions should hopefully speed
up the program and I will be able to include more of them.

[0]: https://en.wikipedia.org/wiki/List_of_countries_by_spoken_languages
[1]: https://github.com/burnash/gspread
