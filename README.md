# Deck.js and dexy

Experimenting with deck.js and dexy.
Combine the two to make presentations that are easy to update on an ongoing basis.

I've used the [grouplens](http://www.grouplens.org/node/12) dataset to provide an example analysis.

## Prerequisites

You need to have [dexy](http://www.dexy.it/) installed on your computer.

```
dexy version
```

Checks that your installation is correct.

You also need to have [pandas](http://pandas.pydata.org/) installed on your machine. This is the library that does all the number crunching.

## How to run the analysis

First, download the grouplens data file `ml-100k.zip` and unzip it somewhere.

All the number crunching is done using the `processdata.py` script. There are a couple of things you need to edit in this script before running the analysis.


### Point to the data directory

Edit the `datadir` variable in the script to point to where you unzipped the grouplens dataset.

```python
datadir = "/home/ewan/Datasets/grouplens/ml-100k/"
```

This directory is the one with all the files like `u.data` and so on.

### Specify which genre of film you want to look at

Edit this line to specify the genre you're interested in.

```python
FILTERGENRE = "Thriller"
```

Genres in the dataset are:

<table>
</table>

<tr>
    <td>
            Animation
    </td>
</tr>
<tr>
    <td>
Children's
    </td>
</tr>
<tr>
    <td>
Comedy
    </td>
</tr>
<tr>
    <td>
Crime 
<tr>
    <td>
Documentary
    </td>
</tr>
<tr>
    <td>
Drama
    </td>
</tr>
<tr>
    <td>
Fantasy
    </td>
</tr>
<tr>
    <td>
Film-Noir 
    </td>
</tr>
<tr>
    <td>
Horror
    </td>
</tr>
<tr>
    <td>
Musical
    </td>
</tr>
<tr>
    <td>
Mystery
    </td>
</tr>
<tr>
    <td>
Romance 
    </td>
</tr>
<tr>
    <td>
Sci-Fi
    </td>
</tr>
<tr>
    <td>
Thriller
    </td>
</tr>
<tr>
    <td>
War
    </td>
</tr>
<tr>
    <td>
Western
    </td>
</tr>


# Run the analysis

Run the command `dexy` in this directory to compile the analysis.

This makes a [deck.js](http://imakewebthings.com/deck.js/) presentation containing all the information in the `output` directory.
